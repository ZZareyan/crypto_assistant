import { create } from "zustand";

interface AppState {
  selectedCoinId: string | null;
  setSelectedCoin: (id: string | null) => void;
}

export const useAppStore = create<AppState>((set) => ({
  selectedCoinId: null,
  setSelectedCoin: (id) => set({ selectedCoinId: id }),
}));
