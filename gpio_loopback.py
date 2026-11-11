import time
import Hobot.GPIO as GPIO

OUT_PIN = 31
IN_PIN = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

try:
    GPIO.setup(OUT_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN_PIN, GPIO.IN)

    print("RDK X5 GPIO Loopback Test")
    print("Output: Pin 31 | Input: Pin 37")

    passed = 0

    for level in [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH]:
        GPIO.output(OUT_PIN, level)
        time.sleep(0.5)

        received = GPIO.input(IN_PIN)
        result = "PASS" if received == level else "FAIL"

        if result == "PASS":
            passed += 1

        print(f"Sent: {level} | Received: {received} | {result}")

    print(f"\nResult: {passed}/4 tests passed")

finally:
    GPIO.cleanup()
