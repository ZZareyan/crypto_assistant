"use client";

import { useQuery } from "@tanstack/react-query";
import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

import { api } from "@/lib/api";

interface Props {
  coinId: string;
  days?: number;
}

export function PriceChart({ coinId, days = 7 }: Props) {
  const { data, isLoading } = useQuery({
    queryKey: ["prices", coinId, days],
    queryFn: () => api.prices.history(coinId, days),
  });

  if (isLoading) {
    return <div className="h-48 animate-pulse rounded-lg bg-gray-100" />;
  }

  return (
    <ResponsiveContainer width="100%" height={192}>
      <LineChart data={data?.ticks ?? []}>
        <XAxis dataKey="recorded_at" hide />
        <YAxis domain={["auto", "auto"]} hide />
        <Tooltip
          formatter={(value: number) => [`$${value.toLocaleString()}`, "Price"]}
          labelFormatter={(label: string) => new Date(label).toLocaleDateString()}
        />
        <Line
          type="monotone"
          dataKey="price_usd"
          dot={false}
          strokeWidth={2}
          stroke="#2563eb"
        />
      </LineChart>
    </ResponsiveContainer>
  );
}
