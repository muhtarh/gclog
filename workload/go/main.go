package main

import "fmt"

const windowSize int = 200000
const msgCount int = 200000
const msgSize int = 28000

func fill(bs [msgSize]byte, b byte) {
	for i, _ := range bs {
		bs[i] = b
	}
}

func createMessage(n int) [msgSize]byte {
	var msg [msgSize]byte
	fill(msg, byte(n))
	return msg
}

func pushMessage(m map[int][msgSize]byte, id int) {
	var lowId int = windowSize - id
	m[id] = createMessage(id)
	if lowId >= 0 {
		delete(m, lowId)
	}
}

func startTask(message string) {
	var m map[int][msgSize]byte = make(map[int][msgSize]byte)
	for i := 0; i < msgCount; i++ {
		pushMessage(m, i)
	}
	fmt.Println(message)
}

func main() {
	fmt.Println("Start ...")
	for i := 0; i < 10; i++ {
		go startTask("Thread num 1")
		startTask("Main thread 1")
		go startTask("Thread num 2")
		startTask("Main thread 2")
	}
	fmt.Println("Finish ...")
}
