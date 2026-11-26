"use client";

import { useEffect, useState } from "react";

export default function Home() {
  // const [health, setHealth] = useState("Indisponible");

  // useEffect(() => {
  //   fetch("/api/health")
  //     .then((r) => r.json())
  //     .then((d) => {
  //       setHealth(d.status);
  //     })
  //     .catch(() => setHealth("Indisponible"));
  // });

  return (
    <div className="border-red-500 border size-full">
      <p>67</p>
    </div>
  );
}
