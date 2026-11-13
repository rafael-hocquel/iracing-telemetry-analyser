"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [health, setHealth] = useState("Indisponible");

  useEffect(() => {
    fetch("/api/health")
      .then((r) => r.json())
      .then((d) => {
        setHealth(d.status);
      })
      .catch(() => setHealth("Indisponible"));
  });

  return (
    <div className="size-full justify-center items-center">
      <p>
        <span className="font-bold">Status: </span>
        {health}
        <span>Some text</span>
        <span className="italic">some italic text</span>
      </p>
    </div>
  );
}
