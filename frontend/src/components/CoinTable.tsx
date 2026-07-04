"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";

import { api, type CoinSummary } from "@/lib/api";

export function CoinTable() {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["coins"],
    queryFn: () => api.coins.list(),
  });

  if (isLoading) {
    return <div className="h-64 animate-pulse rounded-lg bg-gray-100" />;
  }

  if (isError) {
    return <p className="text-red-600">Failed to load coins. Is the backend running?</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b text-left text-gray-500">
            <th className="py-3 pr-4">#</th>
            <th className="py-3 pr-4">Name</th>
            <th className="py-3 pr-4 text-right">Price</th>
            <th className="py-3 pr-4 text-right">24h %</th>
            <th className="py-3 text-right">Market Cap</th>
          </tr>
        </thead>
        <tbody>
          {data?.items.map((coin, i) => (
            <CoinRow key={coin.id} coin={coin} rank={i + 1} />
          ))}
        </tbody>
      </table>
    </div>
  );
}

function CoinRow({ coin, rank }: { coin: CoinSummary; rank: number }) {
  const change = coin.change_24h ?? 0;
  return (
    <tr className="border-b hover:bg-gray-50">
      <td className="py-3 pr-4 text-gray-400">{rank}</td>
      <td className="py-3 pr-4">
        <Link href={`/explore-coins/${coin.id}`} className="flex items-center gap-2 hover:underline">
          {coin.image_url !== null && (
            <img src={coin.image_url} alt={coin.name} className="h-6 w-6 rounded-full" />
          )}
          <span className="font-medium">{coin.name}</span>
          <span className="text-xs uppercase text-gray-400">{coin.symbol}</span>
        </Link>
      </td>
      <td className="py-3 pr-4 text-right">
        {coin.price_usd !== null ? `$${coin.price_usd.toLocaleString()}` : "—"}
      </td>
      <td
        className={`py-3 pr-4 text-right font-medium ${change >= 0 ? "text-green-600" : "text-red-600"}`}
      >
        {change >= 0 ? "+" : ""}
        {change.toFixed(2)}%
      </td>
      <td className="py-3 text-right text-gray-500">
        {coin.market_cap !== null ? `$${(coin.market_cap / 1e9).toFixed(2)}B` : "—"}
      </td>
    </tr>
  );
}
