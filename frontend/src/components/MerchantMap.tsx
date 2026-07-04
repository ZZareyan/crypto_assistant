"use client";

import dynamic from "next/dynamic";

// Leaflet accesses `window` at import time — must be loaded client-side only.
const LeafletMap = dynamic(() => import("./LeafletMap"), {
  ssr: false,
  loading: () => <div className="h-96 animate-pulse rounded-lg bg-gray-100" />,
});

export function MerchantMap() {
  return (
    <div className="overflow-hidden rounded-lg border">
      <LeafletMap />
    </div>
  );
}
