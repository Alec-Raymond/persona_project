import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Persona traces',
  description: 'Replay selected multi-turn Astra conversations and inspect their recorded outputs.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
