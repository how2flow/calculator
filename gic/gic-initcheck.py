#!/usr/bin/env python3

import re

def main():
    print("===================================================")
    print(" GIC Bare-metal Bring-up Check List (with examples)")
    print("===================================================\n")

    print("1. GICD_CTLR[+0x0] (ex: 0x32)")
    print("   - Distributor enable")
    print("   - EnableGrp0 / EnableGrp1")
    print("   - ARE enabled\n")

    print("2. GICR_PWRR[+0x24] (ex: 0x0)")
    print("   - Redistributor power ON\n")

    print("3. GICR_WAKER[+0x14] (ex: 0x0)")
    print("   - ProcessorSleep = 0")
    print("   - ChildrenAsleep = 0\n")

    print("4. GICR_ISENABLER0[+0x10100] (ex: 0x0000FFFF)")
    print("   - SGI/PPI enable\n")

    print("5. GICD_ISENABLERn[+0x100] (ex: 0x00000001)")
    print("   - SPI enable (SPI32+n)\n")

    print("6. GICD_ICFGRn[+0xC00] (ex: 0xAAAAAAAA)")
    print("   - Edge / Level trigger\n")

    print("7. GICD_IPRIORITYRn[+0x400] (ex: 0xA0A0A0A0)")
    print("   - irq priority\n")

    print("8. ICC_SRE_EL3[SPR:0x36CC5] (0x7)")
    print("   - System Register Interface enable\n")

    print("9. ICC_PMR_EL1[SPR:0x30CC5] (0xFF)")
    print("   - Priority Mask max\n")

    print("10. ICC_IGRPEN0_EL1[0x30CC6] (0x1)")
    print("    - Group0 enable\n")

    print("11. ICC_IGRPEN1_EL1[SPR:0x30CC7] (0x1)")
    print("    - Group1 enable\n")

    print("12. GICD_IROUTERn (ex: CPU0 affinity)\n")

    print("===================================================")
    print("※ GIC initialize check list")
    print("===================================================")


if __name__ == "__main__":
    main()
