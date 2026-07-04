const API_BASE = process.env["NEXT_PUBLIC_API_URL"] ?? "http://localhost:8000/api/v1";

async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${res.statusText}`);
  }
  return res.json() as Promise<T>;
}

export interface CoinSummary {
  id: string;
  symbol: string;
  name: string;
  image_url: string | null;
  price_usd: number | null;
  market_cap: number | null;
  change_24h: number | null;
  is_mineable: boolean;
}

export interface CoinDetail extends CoinSummary {
  category: string | null;
  algorithm: string | null;
}

export interface CoinListResponse {
  items: CoinSummary[];
  total: number;
  page: number;
  per_page: number;
}

export interface PriceTick {
  recorded_at: string;
  price_usd: number | null;
  market_cap: number | null;
  volume_24h: number | null;
  change_24h: number | null;
}

export interface PriceHistoryResponse {
  coin_id: string;
  ticks: PriceTick[];
}

export const api = {
  coins: {
    list: (page = 1, perPage = 50, category?: string) => {
      const params = new URLSearchParams({
        page: String(page),
        per_page: String(perPage),
        ...(category !== undefined ? { category } : {}),
      });
      return apiFetch<CoinListResponse>(`/coins/?${params.toString()}`);
    },
    get: (id: string) => apiFetch<CoinDetail>(`/coins/${id}`),
  },
  prices: {
    history: (coinId: string, days = 7) =>
      apiFetch<PriceHistoryResponse>(`/prices/${coinId}/history?days=${days}`),
  },
  mining: {
    coins: () => apiFetch<CoinSummary[]>("/mining/coins"),
  },
  exchanges: {
    list: () => apiFetch<unknown[]>("/exchanges/"),
  },
};
