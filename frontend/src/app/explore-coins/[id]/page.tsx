import type { Metadata } from "next";

import { PriceChart } from "@/components/PriceChart";
import { api } from "@/lib/api";

interface Props {
  params: Promise<{ id: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  const coin = await api.coins.get(id).catch(() => null);
  return { title: coin ? `${coin.name} | Crypto Assistant` : "Coin | Crypto Assistant" };
}

export default async function CoinDetailPage({ params }: Props) {
  const { id } = await params;
  const coin = await api.coins.get(id);

  return (
    <div className="space-y-8">
      <header className="flex items-center gap-4">
        {coin.image_url && (
          <img src={coin.image_url} alt={coin.name} className="h-12 w-12 rounded-full" />
        )}
        <div>
          <h1 className="text-3xl font-bold">{coin.name}</h1>
          <span className="text-lg uppercase text-gray-500">{coin.symbol}</span>
        </div>
      </header>

      <dl className="grid grid-cols-2 gap-4 sm:grid-cols-4">
        <Stat label="Price" value={coin.price_usd != null ? `$${coin.price_usd.toLocaleString()}` : "—"} />
        <Stat
          label="Market Cap"
          value={coin.market_cap != null ? `$${(coin.market_cap / 1e9).toFixed(2)}B` : "—"}
        />
        <Stat
          label="24h Change"
          value={coin.change_24h != null ? `${coin.change_24h.toFixed(2)}%` : "—"}
          positive={coin.change_24h != null && coin.change_24h >= 0}
        />
        {coin.algorithm && <Stat label="Algorithm" value={coin.algorithm} />}
      </dl>

      <section>
        <h2 className="mb-4 text-xl font-semibold">Price History (7d)</h2>
        <PriceChart coinId={coin.id} days={7} />
      </section>
    </div>
  );
}

function Stat({
  label,
  value,
  positive,
}: {
  label: string;
  value: string;
  positive?: boolean;
}) {
  return (
    <div className="rounded-lg border p-4">
      <dt className="text-sm text-gray-500">{label}</dt>
      <dd
        className={`mt-1 text-xl font-semibold ${
          positive === true ? "text-green-600" : positive === false ? "text-red-600" : ""
        }`}
      >
        {value}
      </dd>
    </div>
  );
}
