private static int decodeOctets(int i, ByteBuffer bb, StringBuilder sb) {
    while (i < bb.remaining()) {
        int octet = bb.get(i) & 0xFF;
        if (octet >= 0 && octet <= 127) {
            sb.append((char) octet);
            i++;
        } else if (octet >= 192 && octet <= 223) {
            if (i + 1 < bb.remaining()) {
                int nextOctet = bb.get(i + 1) & 0xFF;
                sb.append((char) (((octet & 0x1F) << 6) | (nextOctet & 0x3F)));
                i += 2;
            } else {
                break; // incomplete byte sequence
            }
        } else if (octet >= 224 && octet <= 239) {
            if (i + 2 < bb.remaining()) {
                int nextOctet1 = bb.get(i + 1) & 0xFF;
                int nextOctet2 = bb.get(i + 2) & 0xFF;
                sb.append((char) (((octet & 0x0F) << 12) | ((nextOctet1 & 0x3F) << 6) | (nextOctet2 & 0x3F)));
                i += 3;
            } else {
                break; // incomplete byte sequence
            }
        } else if (octet >= 240 && octet <= 247) {
            if (i + 3 < bb.remaining()) {
                int nextOctet1 = bb.get(i + 1) & 0xFF;
                int nextOctet2 = bb.get(i + 2) & 0xFF;
                int nextOctet3 = bb.get(i + 3) & 0xFF;
                int codePoint = (((octet & 0x07) << 18) | ((nextOctet1 & 0x3F) << 12) | ((nextOctet2 & 0x3F) << 6) | (nextOctet3 & 0x3F)) - 0x10000;
                sb.append((char) (0xD800 | (codePoint >> 10)));
                sb.append((char) (0xDC00 | (codePoint & 0x3FF)));
                i += 4;
            } else {
                break; // incomplete byte sequence
            }
        } else {
            break; // invalid byte
        }
    }
    return i;
}