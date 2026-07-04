import type { Metadata } from "next";

import { CoinTable } from "@/components/CoinTable";

export const metadata: Metadata = { title: "Explore Coins | Crypto Assistant" };

export default function ExploreCoinsPage() {
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-3xl font-bold">Explore Cryptocurrencies</h1>
        <p className="mt-2 text-gray-600">
          Live prices and market data for the top coins, updated every 5 minutes.
        </p>
      </header>
      <CoinTable />
    </div>
  );
}
