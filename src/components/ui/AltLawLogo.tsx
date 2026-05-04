import { cn } from "@/lib/cn";

type Size = "sm" | "md" | "lg";

const SIZE_TOKENS: Record<
  Size,
  { tile: string; gap: string; plus: string; text: string; wordmark: string }
> = {
  sm: {
    tile: "h-7 w-7 text-base",
    gap: "gap-1",
    plus: "text-sm",
    text: "text-sm",
    wordmark: "text-base",
  },
  md: {
    tile: "h-9 w-9 text-lg",
    gap: "gap-1.5",
    plus: "text-base",
    text: "text-base",
    wordmark: "text-lg",
  },
  lg: {
    tile: "h-12 w-12 text-2xl",
    gap: "gap-2",
    plus: "text-xl",
    text: "text-xl",
    wordmark: "text-2xl",
  },
};

type Props = {
  size?: Size;
  withWordmark?: boolean;
  className?: string;
};

export function AltLawLogo({
  size = "md",
  withWordmark = true,
  className,
}: Props) {
  const t = SIZE_TOKENS[size];

  return (
    <span
      className={cn("inline-flex items-center", t.gap, className)}
      aria-label="Alt+Law"
    >
      <span
        aria-hidden="true"
        className={cn(
          "inline-flex items-center justify-center rounded-md font-semibold tracking-tight",
          "bg-ink text-ink-fg shadow-[0_1px_0_rgba(0,0,0,0.4),inset_0_-2px_0_rgba(0,0,0,0.35)]",
          t.tile,
        )}
      >
        A
      </span>
      <span
        aria-hidden="true"
        className={cn("font-semibold text-text-muted", t.plus)}
      >
        +
      </span>
      <span
        aria-hidden="true"
        className={cn(
          "inline-flex items-center justify-center rounded-md font-semibold tracking-tight",
          "bg-accent text-accent-fg shadow-[0_1px_0_rgba(0,0,0,0.25),inset_0_-2px_0_rgba(0,0,0,0.18)]",
          t.tile,
        )}
      >
        L
      </span>
      {withWordmark && (
        <span className={cn("ml-1 font-semibold tracking-tight", t.wordmark)}>
          Alt
          <span className="text-text-muted font-medium">+</span>
          Law
        </span>
      )}
    </span>
  );
}
