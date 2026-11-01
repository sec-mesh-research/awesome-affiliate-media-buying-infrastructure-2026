#!/usr/bin/env python3
"""
Affiliate Media Buying Full Infrastructure Budget Calculator 2026.
Combines Voluum (Tracker) + AdsPower (Multi-Account Browser) + AdCreative.ai (Assets) + 9Proxy (Proxies).
"""
import argparse

def calculate(monthly_ad_spend, campaigns):
    # Voluum Profit
    voluum_cost = 199.0
    # AdsPower Anti-Detect (50 profiles)
    adspower_cost = 19.0
    # AdCreative.ai Starter (AI creatives)
    adcreative_cost = 59.0
    # 9Proxy (200 residential proxy IPs @ $0.20/IP for campaign landing page verification)
    proxy_cost = 40.0

    total_infra = voluum_cost + adspower_cost + adcreative_cost + proxy_cost
    infra_ratio = (total_infra / monthly_ad_spend) * 100.0

    print("=" * 65)
    print("Affiliate Media Buying Infrastructure Budget Breakdown 2026")
    print("=" * 65)
    print(f"Monthly Media Ad Spend:                 ${monthly_ad_spend:,.2f}")
    print(f"1. Tracking Engine (Voluum Profit):     ${voluum_cost:.2f}/mo")
    print(f"2. Multi-Account Browser (AdsPower):    ${adspower_cost:.2f}/mo")
    print(f"3. AI Creative Suite (AdCreative.ai):   ${adcreative_cost:.2f}/mo")
    print(f"4. Verification Proxies (9Proxy 200p):  ${proxy_cost:.2f}/mo")
    print("-" * 65)
    print(f"Total Dedicated Infrastructure Budget:  ${total_infra:.2f}/mo")
    print(f"Infrastructure as % of Media Spend:     {infra_ratio:.2f}%")
    print("=" * 65)
    return total_infra

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Media Buyer Infra Calculator")
    parser.add_argument("--monthly-ad-spend", type=float, default=10000.0)
    parser.add_argument("--campaigns", type=int, default=15)
    args = parser.parse_args()
    calculate(args.monthly_ad_spend, args.campaigns)
