import type { Metadata } from "next";

import { MiningCalculator } from "@/components/MiningCalculator";

export const metadata: Metadata = { title: "How to Mine | Crypto Assistant" };

const MINEABLE_COINS = [
  { coin: "Bitcoin (BTC)", algorithm: "SHA-256", hardware: "ASIC (e.g., Antminer S21)" },
  { coin: "Litecoin (LTC)", algorithm: "Scrypt", hardware: "ASIC (e.g., Antminer L9)" },
  { coin: "Monero (XMR)", algorithm: "RandomX", hardware: "CPU (ASIC-resistant)" },
  { coin: "Ravencoin (RVN)", algorithm: "KawPow", hardware: "GPU" },
  { coin: "Ergo (ERG)", algorithm: "Autolykos v2", hardware: "GPU" },
  { coin: "Kaspa (KAS)", algorithm: "kHeavyHash", hardware: "ASIC / GPU" },
];

export default function MiningPage() {
  return (
    <div className="space-y-10">
      <header>
        <h1 className="text-3xl font-bold">How to Mine Cryptocurrency</h1>
        <p className="mt-2 text-gray-600">
          Mining means using your hardware to validate transactions and earn freshly minted coins as
          a reward. Not all coins can be mined — only Proof of Work coins apply.
        </p>
      </header>

      <section className="space-y-4">
        <h2 className="text-2xl font-semibold">Mineable Coins</h2>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b text-left">
                <th className="py-2 pr-4">Coin</th>
                <th className="py-2 pr-4">Algorithm</th>
                <th className="py-2">Best Hardware</th>
              </tr>
            </thead>
            <tbody>
              {MINEABLE_COINS.map((row) => (
                <tr key={row.coin} className="border-b">
                  <td className="py-3 pr-4 font-medium">{row.coin}</td>
                  <td className="py-3 pr-4 font-mono text-xs">{row.algorithm}</td>
                  <td className="py-3 text-gray-600">{row.hardware}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="space-y-4">
        <h2 className="text-2xl font-semibold">Profitability Estimator</h2>
        <p className="text-sm text-gray-600">
          Enter your hardware specs to estimate daily electricity cost. For full revenue
          calculations, use{" "}
          <a
            href="https://whattomine.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 underline"
          >
            WhatToMine
          </a>
          .
        </p>
        <div className="max-w-sm">
          <MiningCalculator />
        </div>
      </section>
    </div>
  );
}
