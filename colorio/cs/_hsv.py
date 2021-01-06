import numpy


class HSV:
    def from_srgb1(self, srgb1):
        srgb = numpy.asarray(srgb1, dtype=float)
        orig_shape = srgb.shape
        srgb = srgb.reshape(3, -1)
        assert numpy.all(srgb >= 0)
        assert numpy.all(srgb <= 1)

        argmax = numpy.argmax(srgb, axis=0)
        max_val = numpy.max(srgb, axis=0)
        min_val = numpy.min(srgb, axis=0)

        diff = max_val - min_val

        H = numpy.empty(srgb.shape[1:], dtype=float)
        H[max_val == min_val] = 0
        i = argmax == 0
        H[i] = 60 * (0 + (srgb[1][i] - srgb[2][i]) / diff[i])
        i = argmax == 1
        H[i] = 60 * (2 + (srgb[2][i] - srgb[0][i]) / diff[i])
        i = argmax == 2
        H[i] = 60 * (4 + (srgb[0][i] - srgb[1][i]) / diff[i])
        H = numpy.mod(H, 360)

        S = numpy.empty(srgb.shape[1:], dtype=float)
        S[max_val == 0] = 0
        i = (max_val > 0) & (min_val < 1)
        S[i] = diff[i] / max_val[i]

        H = H.reshape(orig_shape[1:])
        S = S.reshape(orig_shape[1:])
        V = max_val.reshape(orig_shape[1:])
        return numpy.array([H, S, V])

    def to_srgb1(self, hsl):
        H, S, V = hsl
        assert numpy.all(H >= 0)
        assert numpy.all(H <= 360)
        assert numpy.all(S >= 0)
        assert numpy.all(S <= 1)
        assert numpy.all(V >= 0)
        assert numpy.all(V <= 1)

        C = V * S
        H_dash = H / 60
        X = C * (1 - numpy.abs(numpy.mod(H_dash, 2) - 1))
        Z = numpy.zeros(C.shape)

        R1 = numpy.empty(C.shape)
        G1 = numpy.empty(C.shape)
        B1 = numpy.empty(C.shape)
        i = (0 < H_dash) & (H_dash <= 1)
        R1[i], G1[i], B1[i] = C[i], X[i], Z[i]
        i = (1 < H_dash) & (H_dash <= 2)
        R1[i], G1[i], B1[i] = X[i], C[i], Z[i]
        i = (2 < H_dash) & (H_dash <= 3)
        R1[i], G1[i], B1[i] = Z[i], C[i], X[i]
        i = (3 < H_dash) & (H_dash <= 4)
        R1[i], G1[i], B1[i] = Z[i], X[i], C[i]
        i = (4 < H_dash) & (H_dash <= 5)
        R1[i], G1[i], B1[i] = X[i], Z[i], C[i]
        i = (5 < H_dash) & (H_dash <= 6)
        R1[i], G1[i], B1[i] = C[i], Z[i], X[i]

        m = V - C
        return numpy.array([R1 + m, G1 + m, B1 + m])

    def from_srgb256(self, srgb256):
        return self.from_srgb1(numpy.asarray(srgb256) / 255.0)
