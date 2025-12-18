#!/usr/bin/env python3

# ===== User Config (define like) =====
IRQ_MAX = 960
# ====================================

#!/usr/bin/env python3

# ===== User Config =====
IRQ_MAX = 960
# =======================

# ===== GICv3 Distributor Base Offsets =====
GICD_IPRIORITYR = "0x400"
GICD_ICFGR      = "0xC00"
# =========================================

def calc_status(intid):
    offset = (intid // 32) * 4
    bit = intid % 32
    return offset, bit

def calc_icfgr(intid):
    offset = (intid // 16) * 4
    bit = (intid % 16) * 2
    return offset, bit

def calc_priority(intid):
    offset = (intid // 4) * 4
    byte = intid % 4
    return offset, byte

def print_irq_info(intid):
    print(f"\n=== GICv3 IRQ {intid} Register Info ===")

    if intid < 32:
        print("SGI/PPI (0~31) → per-CPU GICR registers")
        return

    if intid > IRQ_MAX:
        print(f"SPI supports up to {IRQ_MAX}")
        return

    # STATUSR (enable / pending / active)
    offset, bit = calc_status(intid)
    print(f"STATUSR             : offset +0x{offset:02X}, bit {bit}")

    # Configuration
    offset, bit = calc_icfgr(intid)
    print(f"ICFGR(+{GICD_ICFGR})       : offset +0x{offset:03X}, bits [{bit+1}:{bit}]")

    # Priority
    offset, byte = calc_priority(intid)
    print(f"IPRIORITYR(+{GICD_IPRIORITYR})  : offset +0x{offset:03X}, byte {byte}")

def main():
    print("GICv3 Distributor IRQ Calculator")
    print("Enter IRQ number (q / quit to exit)")

    while True:
        s = input("\nIRQ ID: ").strip()
        if s.lower() in ("q", "quit"):
            break
        try:
            intid = int(s, 0)
            print_irq_info(intid)
        except ValueError:
            print("Invalid IRQ number")

if __name__ == "__main__":
    main()
