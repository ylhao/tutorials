package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	var str1 = "yilonghao1"
	var str2 = "yilonghao1\nyilonghao2"
	var str3 = `yilonghao3
yilonghao4
yilonghao5
yilonghao6
\n\r\t`
	// 字符串拼接
	str4 := str1 + "," + str1
	fmt.Println(str1)
	fmt.Println(str2)
	fmt.Println(str3)
	fmt.Println(str4)
	// 字符串长度, ascii字符长度
	fmt.Println(len(str1))
	// Unicode 字符串长度
	str5 := "衣龙浩"
	fmt.Println(len(str5))
	fmt.Println(utf8.RuneCountInString(str5))
	// 字符串遍历,ASCII 字符串遍历直接使用下标
	str6 := "yilonghao_衣龙浩"
	for i := 0; i < len(str6); i++ {
		fmt.Printf("ascii: %c, %d\n", str6[i], str6[i])
	}
	// Unicode 字符串遍历用 for range
	for _, s := range str6 {
		fmt.Printf("Unicode: %c, %d\n", s, s)
	}
}
