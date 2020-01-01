package main

import (
	"fmt"
)

// 布尔转整型
func btoi(b bool) int {
	if b {
		return 1
	}
	return 0
}

// 整型转布尔
func itob(n int) bool {
	// n != 0 返回 true
	return n != 0
}

func main() {
	fmt.Println(btoi(true))
	fmt.Println(itob(1))
	fmt.Println(itob(2))
	fmt.Println(itob(0))
}
