import type { ReactNode } from "react";

const GLOSSARY: Record<string, string> = {
  blockchain: "A shared, tamper-proof ledger where every transaction is permanently recorded.",
  wallet: "Software that stores your private keys and lets you send or receive crypto.",
  "private key": "A secret number that proves ownership of your funds. Never share it.",
  "public key": "Your shareable address — like a bank account number for receiving crypto.",
  "gas fee": "A small payment to network validators for processing your transaction.",
  hash: "A fixed-length fingerprint of data, used to link blocks in a blockchain.",
  node: "A computer that participates in the network by storing and validating the blockchain.",
  "proof of work": "A consensus method where miners compete to solve puzzles to add blocks.",
  "proof of stake": "A consensus method where validators stake coins as collateral to add blocks.",
};

interface Props {
  term: string;
  children?: ReactNode;
}

export function GlossaryTooltip({ term, children }: Props) {
  const definition = GLOSSARY[term.toLowerCase()];
  return (
    <span
      className="cursor-help border-b border-dashed border-gray-400"
      title={definition ?? term}
    >
      {children ?? term}
    </span>
  );
}
