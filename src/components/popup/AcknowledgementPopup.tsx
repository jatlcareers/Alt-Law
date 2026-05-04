"use client";

import { useEffect, useRef, useState } from "react";
import { Modal } from "./Modal";

const COOKIE_NAME = "altlaw-aoc-acknowledged";
const ONE_YEAR_SECONDS = 60 * 60 * 24 * 365;

function hasAcknowledged(): boolean {
  if (typeof document === "undefined") return true;
  return document.cookie
    .split(";")
    .some((c) => c.trim().startsWith(`${COOKIE_NAME}=1`));
}

function setAcknowledgedCookie() {
  document.cookie = `${COOKIE_NAME}=1; path=/; max-age=${ONE_YEAR_SECONDS}; SameSite=Lax`;
}

type Props = {
  acknowledgement: string;
};

export function AcknowledgementPopup({ acknowledgement }: Props) {
  const [open, setOpen] = useState(false);
  const acknowledgeBtnRef = useRef<HTMLButtonElement | null>(null);

  useEffect(() => {
    if (!hasAcknowledged()) {
      setOpen(true);
    }
  }, []);

  const handleAcknowledge = () => {
    setAcknowledgedCookie();
    setOpen(false);
  };

  return (
    <Modal
      open={open}
      onClose={handleAcknowledge}
      title="Acknowledgement of Country"
      size="lg"
      showCloseButton={false}
      dismissOnBackdrop={false}
      initialFocusRef={acknowledgeBtnRef}
      footer={
        <div className="flex justify-end">
          <button
            ref={acknowledgeBtnRef}
            type="button"
            onClick={handleAcknowledge}
            className="inline-flex items-center rounded-md bg-accent px-4 py-2 text-sm font-medium text-accent-fg transition-colors hover:bg-accent-hover"
          >
            Acknowledge &amp; continue
          </button>
        </div>
      }
    >
      <p className="text-text">{acknowledgement}</p>
    </Modal>
  );
}
