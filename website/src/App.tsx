import { useEffect, useState } from 'react'
import qmoneyLogo from './assets/qmoney-logo.svg'
import './App.css'

const principles = [
  {
    title: 'No-cloning is the anti-counterfeiting primitive',
    body: 'QMoney uses unclonable quantum states for the note layer, rather than relying only on classical signatures or serial numbers.',
  },
  {
    title: 'Verification is consumptive',
    body: 'A valid note is measured, consumed, and replaced. The system is designed around verify-and-remint rather than endless rechecking of the same token.',
  },
  {
    title: 'Settlement is classical and distributed',
    body: 'Ownership, transfer intent, attestations, and spent-state tracking are handled by a public-key ledger layer inspired by Bitcoin-style system design.',
  },
]

const roadmap = [
  'Preserve the current private-key baseline as an honest reference architecture for transfer, remint, and counterfeit modeling.',
  'Explore separate public-key note families—starting with hidden-subspace prototypes—without pretending the BB84 baseline is already public-key.',
  'Keep new claims grounded with tests, lifecycle invariants, and symbolic checks so conceptual progress stays legible.',
]

type Theme = 'light' | 'dark'

const getInitialTheme = (): Theme => {
  if (typeof window === 'undefined') {
    return 'light'
  }

  const storedTheme = window.localStorage.getItem('qmoney-theme')
  if (storedTheme === 'light' || storedTheme === 'dark') {
    return storedTheme
  }

  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

function ThemeIcon({ theme }: { theme: Theme }) {
  if (theme === 'dark') {
    return (
      <svg aria-hidden="true" viewBox="0 0 24 24" className="icon theme-icon">
        <path
          d="M21 12.8A9 9 0 1 1 11.2 3a7.2 7.2 0 0 0 9.8 9.8Z"
          fill="none"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="1.8"
        />
      </svg>
    )
  }

  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="icon theme-icon">
      <circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" strokeWidth="1.8" />
      <path
        d="M12 2.5v2.2M12 19.3v2.2M21.5 12h-2.2M4.7 12H2.5M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6M18.7 18.7l-1.6-1.6M6.9 6.9 5.3 5.3"
        fill="none"
        stroke="currentColor"
        strokeLinecap="round"
        strokeWidth="1.8"
      />
    </svg>
  )
}

function GithubIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="icon github-icon">
      <path
        d="M12 2C6.48 2 2 6.58 2 12.22c0 4.51 2.87 8.34 6.84 9.69.5.1.68-.22.68-.5 0-.24-.01-1.04-.02-1.88-2.78.62-3.37-1.21-3.37-1.21-.46-1.18-1.11-1.49-1.11-1.49-.91-.64.07-.63.07-.63 1 .07 1.53 1.05 1.53 1.05.9 1.57 2.36 1.12 2.94.86.09-.67.35-1.12.63-1.38-2.22-.26-4.56-1.15-4.56-5.09 0-1.12.39-2.03 1.03-2.74-.1-.26-.45-1.31.1-2.74 0 0 .84-.28 2.75 1.05A9.36 9.36 0 0 1 12 6.84a9.3 9.3 0 0 1 2.5.35c1.9-1.33 2.74-1.05 2.74-1.05.55 1.43.2 2.48.1 2.74.64.71 1.03 1.62 1.03 2.74 0 3.95-2.34 4.83-4.58 5.08.36.32.68.95.68 1.92 0 1.38-.01 2.49-.01 2.83 0 .28.18.61.69.5A10.23 10.23 0 0 0 22 12.22C22 6.58 17.52 2 12 2Z"
        fill="currentColor"
      />
    </svg>
  )
}

function App() {
  const [theme, setTheme] = useState<Theme>(getInitialTheme)

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    document.documentElement.style.colorScheme = theme
    window.localStorage.setItem('qmoney-theme', theme)
  }, [theme])

  const nextTheme = theme === 'light' ? 'dark' : 'light'

  return (
    <div className="page">
      <header className="site-header">
        <a className="brand" href="#top" aria-label="QMoney home">
          <span className="brand-mark">
            <img src={qmoneyLogo} alt="QMoney logo" className="brand-logo" />
          </span>
          <span>QMoney</span>
        </a>

        <div className="header-controls">
          <nav className="site-nav" aria-label="Primary navigation">
            <a href="#premise">Premise</a>
            <a href="#roadmap">Roadmap</a>
            <a href="#contact">Join</a>
          </nav>

          <div className="header-actions">
            <a
              className="icon-link"
              href="https://github.com/runeape-sats/qmoney"
              target="_blank"
              rel="noreferrer"
              aria-label="GitHub"
            >
              <GithubIcon />
              <span>GitHub</span>
            </a>

            <button
              type="button"
              className="icon-button"
              aria-label={`Switch to ${nextTheme} mode`}
              onClick={() => setTheme(nextTheme)}
            >
              <ThemeIcon theme={theme} />
            </button>
          </div>
        </div>
      </header>

      <main id="top">
        <section className="hero">
          <p className="eyebrow">Quantum Computing + Bitcoin research</p>
          <h1>QMoney: A Peer-to-Peer Quantum Money System</h1>
          <p className="lede">
            The core idea is to use <strong>no-cloning</strong> for the quantum anti-counterfeiting
            layer, then use a <strong>Bitcoin-like classical settlement layer</strong> for ownership
            transfer, attestations, and spent-state tracking. The current system is best understood
            as <strong>quorum-verified private-key quantum cash</strong> with
            <strong> verify-and-remint</strong> semantics.
          </p>

          <div className="hero-actions">
            <a className="button button-primary" href="#premise">
              Read the premise
            </a>
            <a className="button button-secondary" href="#contact">
              Join the journey
            </a>
            <a
              className="button button-secondary button-github"
              href="https://github.com/runeape-sats/qmoney"
              target="_blank"
              rel="noreferrer"
            >
              <GithubIcon />
              <span>View on GitHub</span>
            </a>
          </div>
        </section>

        <section className="stats" aria-label="QMoney highlights">
          <article>
            <span className="stat-value">2</span>
            <span className="stat-label">layers: quantum note validity and classical settlement</span>
          </article>
          <article>
            <span className="stat-value">1</span>
            <span className="stat-label">core transfer model: verify, consume, then remint</span>
          </article>
          <article>
            <span className="stat-value">11</span>
            <span className="stat-label">current tests covering runtime behavior and oracle invariants</span>
          </article>
        </section>

        <section className="section" id="premise">
          <div className="section-copy">
            <p className="section-kicker">Premise</p>
            <h2>Quantum and classical layers do different jobs.</h2>
            <p className="section-body">
              The quantum note layer is where anti-counterfeiting lives: BB84-style notes,
              hidden verification data, and consumptive verification. The classical layer is where
              circulation lives: owner keys, signed transfer intent, quorum attestations, and
              spent-state tracking. Classical public-key cryptography helps coordinate settlement,
              but it does not turn the note family into public-key quantum money.
            </p>
          </div>

          <div className="architecture-grid">
            {principles.map((item, index) => (
              <article className={`panel${index === 0 ? ' panel-strong' : ''}`} key={item.title}>
                <p className="panel-label">Core idea</p>
                <h3>{item.title}</h3>
                <p>{item.body}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="section" id="roadmap">
          <div className="section-copy narrow">
            <p className="section-kicker">Roadmap</p>
          </div>

          <ol className="roadmap-list">
            {roadmap.map((item, index) => (
              <li className="roadmap-item" key={item}>
                <span className="roadmap-index">0{index + 1}</span>
                <p>{item}</p>
              </li>
            ))}
          </ol>
        </section>

        <section className="closing panel" id="contact">
          <p className="section-kicker">Join the journey</p>
          <h2>If quantum computing and Bitcoin both fascinate you, QMoney is an invitation to explore where they might meet.</h2>
          <p>
            We are building in public for people who care about cryptography, distributed systems,
            quantum information, and the future of money. If that sounds like your kind of frontier,
            come follow the work, think alongside it, and help shape what this experiment becomes.
          </p>
        </section>
      </main>
    </div>
  )
}

export default App
