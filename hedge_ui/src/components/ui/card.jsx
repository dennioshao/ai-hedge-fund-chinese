// src/components/ui/card.jsx
import React from "react";
import clsx from "clsx";

export function Card({ className, children }) {
  return (
    <div className={clsx("bg-white shadow-md rounded-lg p-4", className)}>
      {children}
    </div>
  );
}

export function CardContent({ className, children }) {
  return <div className={clsx("space-y-2", className)}>{children}</div>;
}
