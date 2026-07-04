import type { Metadata } from "next";

import { ExchangeComparison } from "@/components/ExchangeComparison";

export const metadata: Metadata = { title: "How to Buy | Crypto Assistant" };

const STEPS = [
  "Create an account on a centralised exchange and complete identity verification (KYC).",
  "Deposit fiat via bank transfer or debit card.",
  "Search for the coin and place a market order (instant) or limit order (at your target price).",
  "Confirm the purchase and note the transaction fee.",
  "For amounts above ~$500, withdraw to a hardware wallet you control.",
];

export default function HowToBuyPage() {
  return (
    <div className="space-y-10">
      <header>
        <h1 className="text-3xl font-bold">How to Buy Cryptocurrency</h1>
        <p className="mt-2 text-gray-600">
          The safest path from fiat currency to crypto in five steps.
        </p>
      </header>

      <section className="space-y-4">
        <h2 className="text-2xl font-semibold">Step-by-Step</h2>
        <ol className="space-y-3">
          {STEPS.map((step, i) => (
            <li key={i} className="flex gap-3">
              <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-blue-100 text-sm font-bold text-blue-700">
                {i + 1}
              </span>
              <span className="text-gray-700">{step}</span>
            </li>
          ))}
        </ol>
      </section>

      <section className="space-y-4">
        <h2 className="text-2xl font-semibold">Compare Exchanges</h2>
        <ExchangeComparison />
      </section>

      <section className="space-y-3">
        <h2 className="text-2xl font-semibold">Wallet Recommendations</h2>
        <div className="grid gap-4 sm:grid-cols-2">
          <div className="rounded-lg border p-4">
            <h3 className="font-semibold">Hot Wallets (Software)</h3>
            <ul className="mt-2 space-y-1 text-sm text-gray-600">
              <li>MetaMask — Ethereum & EVM chains</li>
              <li>Exodus — multi-chain desktop/mobile</li>
              <li>Trust Wallet — mobile, multi-chain</li>
            </ul>
          </div>
          <div className="rounded-lg border p-4">
            <h3 className="font-semibold">Cold Wallets (Hardware)</h3>
            <ul className="mt-2 space-y-1 text-sm text-gray-600">
              <li>Ledger Nano X — Bluetooth, 5500+ coins</li>
              <li>Trezor Model T — open source firmware</li>
            </ul>
            <p className="mt-2 text-xs text-gray-500">Recommended for balances above ~$500</p>
          </div>
        </div>
      </section>
    </div>
  );
}
