func reverseBits(num uint32) uint32 {
	x := strconv.FormatUint(uint64(num), 2)
	n := len(x)
	temp := []rune(x)
	chars := []rune(x)

	for i := 0; i < n/2; i++ {
		chars[i], chars[n-1-i] = temp[n-1-i], temp[i]
	}
	rev_str := string(chars)
	for i := 0; i < 32-len(x); i++ {
		rev_str += "0"
	}
	// fmt.Println(rev_str)
	rev_int, _ := strconv.ParseInt(rev_str, 2, 64)

	return uint32(rev_int)
}
