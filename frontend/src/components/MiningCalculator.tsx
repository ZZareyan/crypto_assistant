"use client";

import { useState } from "react";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

const schema = z.object({
  hashrate: z.number().positive("Must be positive"),
  power: z.number().positive("Must be positive"),
  electricityCost: z.number().min(0, "Cannot be negative"),
});

type FormValues = z.infer<typeof schema>;

export function MiningCalculator() {
  const [dailyCost, setDailyCost] = useState<number | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const onSubmit = (values: FormValues) => {
    setDailyCost((values.power / 1000) * 24 * values.electricityCost);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <Field
        label="Hashrate (MH/s)"
        error={errors.hashrate?.message}
        input={<input type="number" step="0.01" {...register("hashrate", { valueAsNumber: true })} className="input" />}
      />
      <Field
        label="Power draw (W)"
        error={errors.power?.message}
        input={<input type="number" {...register("power", { valueAsNumber: true })} className="input" />}
      />
      <Field
        label="Electricity cost ($/kWh)"
        error={errors.electricityCost?.message}
        input={<input type="number" step="0.001" {...register("electricityCost", { valueAsNumber: true })} className="input" />}
      />
      <button
        type="submit"
        className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
      >
        Estimate
      </button>
      {dailyCost !== null && (
        <p className="text-sm">
          Daily electricity cost:{" "}
          <strong className="text-red-600">${dailyCost.toFixed(2)}</strong>
        </p>
      )}
    </form>
  );
}

function Field({
  label,
  error,
  input,
}: {
  label: string;
  error?: string;
  input: React.ReactNode;
}) {
  return (
    <div>
      <label className="mb-1 block text-sm font-medium text-gray-700">{label}</label>
      {input}
      {error !== undefined && <p className="mt-1 text-xs text-red-600">{error}</p>}
    </div>
  );
}
