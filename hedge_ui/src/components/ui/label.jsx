// src/components/ui/label.jsx
import React from "react";
import clsx from "clsx";

export function Label({ className, children, ...props }) {
  return (
    <label
      className={clsx("block text-sm font-medium text-gray-700", className)}
      {...props}
    >
      {children}
    </label>
  );
}
