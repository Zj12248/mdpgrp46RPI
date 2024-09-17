from communication.stm32 import STMLink 
# STM32 BOARD SERIAL CONNECTION
# to get connected serial devices: ls /dev/serial/by-id/
# SERIAL_PORT = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0002-if00-port0"  # stm32
# BAUD_RATE = 115200

def main():
    # Initialize the STMLink object
    stm_link = STMLink()
    
    # Connect to STM32
    try:
        stm_link.connect()
        print("Connected to STM32 successfully.")
        
        # Test sending a command to STM32
        test_command = "FW01"  # Move forward 1 unit as an example command
        print(f"Sending command to STM32: {test_command}")
        stm_link.send(test_command)
        
        # Wait for acknowledgment from STM32
        ack = stm_link.recv()
        if ack == "ACK":
            print("STM32 acknowledged the command.")
        else:
            print(f"Unexpected response from STM32: {ack}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Disconnect from STM32
        stm_link.disconnect()
        print("Disconnected from STM32.")

if __name__ == "__main__":
    main()
