#!/usr/bin/env python3

def main():
    print("===================================================")
    print(" GICv3 ITS & LPI Bring-up Check List (T32 Style)")
    print("===================================================\n")

    print("--- Redistributor (GICR) LPI Config ---")

    print("0. GICR_TYPER[+0x08] (Read-Only)")
    print("   - [25:24] CommonLPIAff (0=Aff3, 1=Aff3.Aff2, 2=Aff3.Aff2.Aff1, 3=Unique)")
    print("   - [26]    VLPIS (Virtual LPI support)\n")

    print("1. GICR_PROPBASER[+0x70] (ex: 0x... Physical Addr)")
    print("   - [63:12] Physical Address (4KB aligned)")
    print("   - [11:10] Shareability (ex: 0x1=Inner Shareable)")
    print("   - [9:7]   Inner Cache (ex: 0x1=WBWA)")
    print("   - [4:0]   IDBits (ex: 0xd => 14bits => 16K LPIs)")
    print("   ! WARNING: Do NOT write if EnableLPIs==1\n")

    print("2. GICR_PENDBASER[+0x78] (ex: 0x... Physical Addr)")
    print("   - [63:16] Physical Address (64KB aligned)")
    print("   - [62]    PTZ (Pending Table Zero) - optimization")
    print("   - [11:10] Shareability")
    print("   - [9:7]   Inner Cache")
    print("   ! WARNING: Do NOT write if EnableLPIs==1\n")

    print("3. GICR_CTLR[+0x00] (ex: 0x0 -> 0x1)")
    print("   - [0] EnableLPIs (0: Disabled, 1: Enabled)")
    print("   ! NOTE: Ensure Table setup & Cache Clean before setting 1\n")

    print("--- ITS (GITS) Config ---")

    print("0. GITS_TYPER[+0x08] (Read-Only)")
    print("   - [19]    PTA (Physical Target Address support)")
    print("   - [17:13] Devbits (DeviceID width - 1)")
    print("   - [12:8]  IDbits (EventID width - 1)\n")

    print("4. GITS_CBASER[+0x80] (ex: 0x80... Valid)")
    print("   - [63]    Valid")
    print("   - [51:12] Physical Address (Cmd Queue Base)")
    print("   - [7:0]   Size (Size in 4KB pages - 1)\n")

    print("5. GITS_CWRITER[+0x88] (ex: 0x0)")
    print("   - [19:5]  Offset (Command Queue Write Pointer)\n")

    print("6. GITS_CREADR[+0x90] (ex: 0x0)")
    print("   - [19:5]  Offset (Command Queue Read Pointer)\n")

    print("7. GITS_BASER<n>[+0x100 + 8*n] (Device/Collection Tables)")
    print("   - [63]    Valid")
    print("   - [62]    Indirect")
    print("   - [58:56] Page Size (0=4KB, 1=16KB, 2=64KB)")
    print("   - [47:12] Physical Address")
    print("   - [7:0]   Size (Number of pages - 1)\n")

    print("8. GITS_CTLR[+0x00] (ex: 0x1)")
    print("   - [0] Enabled (ITS Enable)")
    print("   - [31] Quiescent (Read-only, 1=Idle)\n")

    print("===================================================")
    print("※ Runtime Check: EnableLPIs=1 + GITS_CTLR=1")
    print("   - LPI update: MemWrite -> CacheClean -> INV/INVALL")
    print("===================================================")

if __name__ == "__main__":
    main()
