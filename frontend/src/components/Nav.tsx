import Link from "next/link";

const LINKS = [
  { href: "/what-is-crypto", label: "What Is Crypto" },
  { href: "/explore-coins", label: "Explore Coins" },
  { href: "/mining", label: "Mining" },
  { href: "/how-to-buy", label: "How to Buy" },
  { href: "/how-to-spend", label: "How to Spend" },
];

export function Nav() {
  return (
    <nav className="border-b">
      <div className="mx-auto flex max-w-6xl items-center gap-6 px-4 py-3">
        <Link href="/" className="text-lg font-bold tracking-tight">
          Crypto Assistant
        </Link>
        <ul className="flex gap-4">
          {LINKS.map((link) => (
            <li key={link.href}>
              <Link
                href={link.href}
                className="text-sm text-gray-600 hover:text-gray-900"
              >
                {link.label}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}
