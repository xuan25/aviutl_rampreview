package main

import (
	"flag"

	"ZRamPreview/ipc"
	"ZRamPreview/ods"
)

func main() {
	defer func() {
		if err := recover(); err != nil {
			ods.Recover(err)
		}
	}()

	flag.Parse()

	ipcm := ipc.New()
	exitCh := make(chan struct{})
	ipcm.Main(exitCh)
}
