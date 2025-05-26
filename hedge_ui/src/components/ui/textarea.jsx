// src/components/ui/textarea.jsx
import React from "react";
import clsx from "clsx";

export function Textarea({ className, ...props }) {
  return (
    <textarea
      className={clsx(
        "w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400",
        className
      )}
      {...props}
    />
  );
}
