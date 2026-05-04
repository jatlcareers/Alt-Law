import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { cn } from "@/lib/cn";

type Props = {
  children: string;
  className?: string;
  /** Render block-level container with prose-body styling */
  withProseStyles?: boolean;
};

export function Markdown({ children, className, withProseStyles = true }: Props) {
  return (
    <div className={cn(withProseStyles && "prose-body", className)}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ href, children, ...rest }) => {
            const isExternal =
              !!href && /^(https?:|mailto:|tel:)/i.test(href);
            return (
              <a
                href={href}
                target={isExternal ? "_blank" : undefined}
                rel={isExternal ? "noopener noreferrer" : undefined}
                {...rest}
              >
                {children}
              </a>
            );
          },
        }}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
