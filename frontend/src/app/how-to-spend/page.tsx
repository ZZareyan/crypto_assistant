import type { Metadata } from "next";

import { MerchantMap } from "@/components/MerchantMap";

export const metadata: Metadata = { title: "How to Spend | Crypto Assistant" };

const METHODS = [
  {
    method: "Crypto debit card",
    how: "Converts crypto to fiat at checkout automatically",
    examples: "Coinbase Card, Crypto.com Visa, Bitpay Card",
  },
  {
    method: "BitPay merchants",
    how: "Direct crypto checkout at point of sale",
    examples: "Newegg, Shopify stores",
  },
  {
    method: "Lightning Network",
    how: "Instant, near-zero fee Bitcoin payments",
    examples: "Strike, Cash App, many online stores",
  },
  {
    method: "Stablecoin transfer",
    how: "Send USDC/USDT like a bank transfer",
    examples: "Freelance payments, remittances",
  },
  {
    method: "Gift cards",
    how: "Buy gift cards with crypto",
    examples: "Bitrefill, CoinGate",
  },
];

export default function HowToSpendPage() {
  return (
    <div className="space-y-10">
      <header>
        <h1 className="text-3xl font-bold">How to Spend Cryptocurrency</h1>
        <p className="mt-2 text-gray-600">
          Crypto is spendable today — here&apos;s how. Note: spending crypto is a taxable event in
          most jurisdictions. Check your local law.
        </p>
      </header>

      <section className="space-y-4">
        <h2 className="text-2xl font-semibold">Ways to Spend</h2>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b text-left">
                <th className="py-2 pr-4">Method</th>
                <th className="py-2 pr-4">How it works</th>
                <th className="py-2">Examples</th>
              </tr>
            </thead>
            <tbody>
              {METHODS.map((row) => (
                <tr key={row.method} className="border-b">
                  <td className="py-3 pr-4 font-medium">{row.method}</td>
                  <td className="py-3 pr-4 text-gray-600">{row.how}</td>
                  <td className="py-3 text-gray-500">{row.examples}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="space-y-4">
        <h2 className="text-2xl font-semibold">Find Local Merchants</h2>
        <p className="text-sm text-gray-600">
          The map below shows businesses near you that accept crypto directly.
        </p>
        <MerchantMap />
      </section>
    </div>
  );
}
