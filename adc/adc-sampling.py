#!/usr/bin/env python3

import argparse

# ===== User Config (define like) =====
VREF = 1.8        # Reference Voltage
ADC_BITS = 12     # ADC Resolution (bits)
# ====================================

ADC_MAX = (1 << ADC_BITS) - 1


def voltage_to_adc(v):
    adc = int(round(v * ADC_MAX / VREF))
    return max(0, min(ADC_MAX, adc))


def adc_to_voltage(adc):
    return adc * VREF / ADC_MAX


def interactive_voltage_mode():
    print(f"Voltage → ADC mode ({ADC_BITS}-bit, Vref={VREF}V)")
    print("q / quit to exit\n")

    while True:
        s = input("Voltage (V): ").strip()
        if s.lower() in ("q", "quit"):
            break
        try:
            v = float(s)
            adc = voltage_to_adc(v)
            print(f"  [{ADC_BITS}-bit ADC]")
            print(f"  ADC(dec): {adc}")
            print(f"  ADC(hex): 0x{adc:0{(ADC_BITS+3)//4}X}")
        except ValueError:
            print("  Invalid voltage\n")


def interactive_adc_mode():
    print(f"ADC → Voltage mode ({ADC_BITS}-bit, Vref={VREF}V)")
    print("q / quit to exit\n")

    while True:
        s = input("ADC value (dec / hex): ").strip()
        if s.lower() in ("q", "quit"):
            break
        try:
            adc = int(s, 0)
            adc = max(0, min(ADC_MAX, adc))
            v = adc_to_voltage(adc)
            print(f"  [{ADC_BITS}-bit ADC]")
            print(f"  Voltage: {v:.6f} V")
        except ValueError:
            print("  Invalid ADC value\n")


def main():
    parser = argparse.ArgumentParser(
        description="Interactive ADC Converter"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-v", "--voltage", action="store_true",
                       help="Voltage → ADC")
    group.add_argument("-a", "--adc", action="store_true",
                       help="ADC → Voltage")
    args = parser.parse_args()

    if args.voltage:
        interactive_voltage_mode()
    else:
        interactive_adc_mode()


if __name__ == "__main__":
    main()
