"use client";

import { Modal } from "./Modal";
import { Markdown } from "@/components/ui/Markdown";

type Props = {
  open: boolean;
  onClose: () => void;
  title: string;
  body: string;
  byline?: string;
  size?: "md" | "lg" | "xl";
};

export function ResourceModal({
  open,
  onClose,
  title,
  body,
  byline,
  size = "lg",
}: Props) {
  return (
    <Modal open={open} onClose={onClose} title={title} size={size}>
      {byline && (
        <p className="mb-3 text-sm font-medium uppercase tracking-[0.12em] text-text-subtle">
          {byline}
        </p>
      )}
      <Markdown>{body}</Markdown>
    </Modal>
  );
}
