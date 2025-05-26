// src/components/ui/button.jsx
import React from "react";
import clsx from "clsx";

export function Button({ className, ...props }) {
  return (
    <button
      className={clsx(
        "bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded disabled:opacity-50",
        className
      )}
      {...props}
    />
  );
}
