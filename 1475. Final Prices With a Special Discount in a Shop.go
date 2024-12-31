func finalPrices(prices []int) []int {
    arrLen := len(prices)
	for i:=0; i<arrLen; i++{
		for j:=i+1; j<arrLen; j++{
			if prices[i]>= prices[j]{
				prices[i] = prices[i] - prices[j]
				break
			}
		}
	} 
	return prices
}
