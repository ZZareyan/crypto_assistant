import Link from "next/link";

const SECTIONS = [
  {
    href: "/what-is-crypto",
    title: "What Is Crypto?",
    description: "Learn how blockchain works, what wallets are, and why crypto is decentralized.",
    icon: "🔗",
  },
  {
    href: "/explore-coins",
    title: "Explore Coins",
    description: "Browse live prices, market caps, and details for thousands of cryptocurrencies.",
    icon: "📊",
  },
  {
    href: "/mining",
    title: "How to Mine",
    description: "Discover which coins you can mine and estimate profitability for your hardware.",
    icon: "⛏️",
  },
  {
    href: "/how-to-buy",
    title: "How to Buy",
    description: "Compare exchanges, understand order types, and keep your funds secure.",
    icon: "💳",
  },
  {
    href: "/how-to-spend",
    title: "How to Spend",
    description: "Find merchants, set up a crypto debit card, and use Lightning Network payments.",
    icon: "🛒",
  },
];

export default function HomePage() {
  return (
    <div className="space-y-12">
      <header className="space-y-4 text-center">
        <h1 className="text-4xl font-bold tracking-tight">Crypto Assistant</h1>
        <p className="mx-auto max-w-xl text-lg text-gray-600">
          A complete beginner&apos;s guide to cryptocurrency — from first principles to spending
          your first coins.
        </p>
      </header>

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {SECTIONS.map((section) => (
          <Link
            key={section.href}
            href={section.href}
            className="group rounded-xl border p-6 transition-shadow hover:shadow-md"
          >
            <div className="mb-3 text-3xl">{section.icon}</div>
            <h2 className="mb-2 text-xl font-semibold group-hover:text-blue-600">
              {section.title}
            </h2>
            <p className="text-sm text-gray-600">{section.description}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
