import type { Metadata } from "next";

import { GlossaryTooltip } from "@/components/GlossaryTooltip";

export const metadata: Metadata = { title: "What Is Crypto? | Crypto Assistant" };

export default function WhatIsCryptoPage() {
  return (
    <article className="prose prose-gray max-w-3xl">
      <h1>What Is Cryptocurrency?</h1>

      <p>
        A cryptocurrency is digital money that exists only on the internet — no bank or government
        controls it. Every transaction is recorded on a{" "}
        <GlossaryTooltip term="blockchain" />, a shared ledger that thousands of computers around
        the world maintain simultaneously.
      </p>

      <h2>How a Transaction Works</h2>
      <ol>
        <li>You sign a transaction with your <GlossaryTooltip term="private key" />.</li>
        <li>The transaction is broadcast to the network.</li>
        <li>
          Validators (miners or stakers) bundle it into a block and add it to the chain.
        </li>
        <li>
          You pay a small <GlossaryTooltip term="gas fee" /> to the validator for their work.
        </li>
        <li>
          The recipient can now see the funds in their <GlossaryTooltip term="wallet" />.
        </li>
      </ol>

      <h2>Proof of Work vs Proof of Stake</h2>
      <p>
        <GlossaryTooltip term="proof of work">Proof of Work</GlossaryTooltip> (Bitcoin) requires
        miners to burn electricity solving puzzles. The winner adds the next block and earns the
        reward. It is energy-intensive but battle-tested.
      </p>
      <p>
        <GlossaryTooltip term="proof of stake">Proof of Stake</GlossaryTooltip> (Ethereum
        post-Merge) requires validators to lock up coins as collateral. A validator is chosen at
        random weighted by stake. Far more energy-efficient.
      </p>

      <h2>Key Terms</h2>
      <ul>
        <li><strong>Wallet</strong> — <GlossaryTooltip term="wallet" /></li>
        <li><strong>Hash</strong> — <GlossaryTooltip term="hash" /></li>
        <li><strong>Node</strong> — <GlossaryTooltip term="node" /></li>
        <li><strong>Gas fee</strong> — <GlossaryTooltip term="gas fee" /></li>
      </ul>
    </article>
  );
}
