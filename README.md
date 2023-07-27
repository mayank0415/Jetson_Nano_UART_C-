Uart Communication in between Jetson Nano to STM32 microcontroller (ROS board) via /dev/ttyUSB0 port.

Initialize UART in your main =>> Uart uart;

Send string buffer by using =>> uart.sendUart(send_str);

read string buffer by using =>> uart.readUart();