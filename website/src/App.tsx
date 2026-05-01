import { useEffect, useState } from 'react'
import qmoneyLogo from './assets/qmoney-logo.svg'
import './App.css'

const introPoints = [
  {
    title: 'Distributed private-key quantum cash',
    body: 'QMoney is a work-in-progress research repo for distributed private-key quantum cash, not a finished public-key quantum money system.',
  },
  {
    title: 'Quantum anti-counterfeiting + classical settlement',
    body: 'The design uses no-cloning for the note layer and a Bitcoin-inspired classical layer for ownership transfer, attestations, and spent-state tracking.',
  },
  {
    title: 'Verify-and-remint baseline',
    body: 'The current baseline is quorum-verified, private-key quantum cash with verify-and-remint semantics rather than a forever-reusable self-verifying note.',
  },
]

const historyPoints = [
  'Wiesner wrote the core idea in the late 1960s, long before quantum money became a mainstream research topic.',
  'The original manuscript was rejected and shelved for years before finally appearing in 1983, which makes quantum money one of the field’s earliest “too early” ideas.',
  'No-cloning was already part of Wiesner’s cryptographic intuition before the no-cloning theorem was formally published in 1982.',
  'The line from Wiesner to BB84 is direct: the same conceptual seed helped launch modern quantum cryptography.',
  'Private-key quantum money came first, which is why QMoney keeps today’s private-key baseline clearly separate from future public-key ambitions.',
]

const currentReferences = [
  {
    category: 'Architecture',
    items: [
      {
        title: 'Public vs private key QMoney',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/public-vs-private-key-qmoney.md',
        description: 'Canonical statement of why the current repo is private-key quantum cash rather than public-key quantum money.',
      },
      {
        title: 'Software MPS quorum design',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/software-mps-quorum-design.md',
        description: 'Technical appendix for the current software-only MPS/quorum baseline and protocol flow.',
      },
      {
        title: 'Private-key quorum threat model',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/private-key-quorum-threat-model.md',
        description: 'Threat model for the private-key quorum baseline, including adversaries, quorum assumptions, remint failure modes, and noise/tolerance questions.',
      },
      {
        title: 'Public-key implementation workflow',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/public-key-implementation-workflow.md',
        description: 'Implementation source of truth for the future public-key/oracle track.',
      },
    ],
  },
  {
    category: 'Research',
    items: [
      {
        title: 'Latest quantum money literature and QMoney',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/research/latest-quantum-money-literature-and-qmoney.md',
        description: 'Survey of the most relevant recent literature for QMoney’s architecture and research direction.',
      },
      {
        title: 'Quantum money literature roadmap',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/research/quantum-money-literature-roadmap.md',
        description: 'Ranked reading and prototyping roadmap for what QMoney should study, build, monitor, and avoid next.',
      },
      {
        title: 'Wiesner counterfeiting attacks and QMoney',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/research/wiesner-counterfeiting-attacks-and-qmoney.md',
        description: 'Why one-note-to-two-notes counterfeiting attacks are a strong fit for the current private-key baseline.',
      },
      {
        title: 'Ekert quantum cryptography and QMoney',
        href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/research/ekert-quantum-cryptography-and-qmoney.md',
        description: 'Review of Bell-certified security, entanglement-based key exchange, noisy-channel privacy amplification, and what Ekert’s cryptography ideas imply for QMoney.',
      },
    ],
  },
]

const comparisonRows = [
  {
    dimension: 'Thing being spent',
    pkey: 'BB84-style private-key bill: serial + qubits',
    pubkey: 'Hidden-subspace note: serial + quantum state over a subspace',
    bitcoin: 'One or more UTXOs',
  },
  {
    dimension: 'Ownership proof',
    pkey: 'Possession of a valid bill plus ledger claimant check',
    pubkey: 'Possession of a note that passes public hidden-subspace verification',
    bitcoin: 'Digital signature from the private key controlling the UTXO',
  },
  {
    dimension: 'Verification',
    pkey: 'Private quorum nodes check hidden per-qubit basis/bit secrets',
    pubkey: 'Public verifier checks subspace and dual-subspace structure/oracles',
    bitcoin: 'Anyone checks signatures, scripts, UTXO existence, and consensus rules',
  },
  {
    dimension: 'Transfer model',
    pkey: 'Verify old bill, consume it by measurement, mint a fresh bill to the receiver',
    pubkey: 'Research model verifies a note against public key/oracle publication',
    bitcoin: 'Consume old UTXOs, create new UTXOs',
  },
  {
    dimension: 'Double-spend prevention',
    pkey: 'Local Ledger marks serials spent',
    pubkey: 'Not fully modeled as production settlement yet',
    bitcoin: 'Global consensus and UTXO-set validation',
  },
  {
    dimension: 'Trust model',
    pkey: 'Requires quorum nodes to hold secrets and be available',
    pubkey: 'Aims toward public verification, but the current prototype exposes too much structure',
    bitcoin: 'Trust-minimized public validation by full nodes',
  },
  {
    dimension: 'Who can verify',
    pkey: 'Only quorum participants with the bill secrets',
    pubkey: 'Anyone with the public key/oracle publication in the model',
    bitcoin: 'Anyone running a Bitcoin verifier/full node',
  },
  {
    dimension: 'Counterfeit resistance',
    pkey: 'BB84 disturbance/no-cloning intuition in a private-key setting',
    pubkey: 'Hidden-subspace quantum money idea, without a current unforgeability claim',
    bitcoin: 'Signature unforgeability plus consensus against double spends',
  },
  {
    dimension: 'Current repo status',
    pkey: 'Current private-key baseline',
    pubkey: 'Research-only prototype, tiny n, conceptual clarity over cryptographic realism',
    bitcoin: 'Real production protocol',
  },
  {
    dimension: 'Main caveat',
    pkey: 'Trusted/private verifier quorum',
    pubkey: 'Current public key publishes enough structure to reconstruct an accepting note',
    bitcoin: 'Requires network fees, block inclusion, and probabilistic finality',
  },
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

function MenuIcon({ open }: { open: boolean }) {
  if (open) {
    return (
      <svg aria-hidden="true" viewBox="0 0 24 24" className="icon menu-icon">
        <path d="M6 6 18 18M18 6 6 18" fill="none" stroke="currentColor" strokeLinecap="round" strokeWidth="1.8" />
      </svg>
    )
  }

  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="icon menu-icon">
      <path d="M4 7.5h16M4 12h16M4 16.5h16" fill="none" stroke="currentColor" strokeLinecap="round" strokeWidth="1.8" />
    </svg>
  )
}

function App() {
  const [theme, setTheme] = useState<Theme>(getInitialTheme)
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    document.documentElement.style.colorScheme = theme
    window.localStorage.setItem('qmoney-theme', theme)
  }, [theme])

  useEffect(() => {
    const closeMenu = () => setIsMobileMenuOpen(false)
    window.addEventListener('resize', closeMenu)
    return () => window.removeEventListener('resize', closeMenu)
  }, [])

  const nextTheme = theme === 'light' ? 'dark' : 'light'
  const menuLabel = isMobileMenuOpen ? 'Close site menu' : 'Open site menu'
  const handleMenuToggle = () => setIsMobileMenuOpen((open) => !open)
  const handleMobileNavClick = () => setIsMobileMenuOpen(false)

  return (
    <div className="page">
      <header className="site-header">
        <div className="header-top-row">
          <a className="brand" href="#top" aria-label="QMoney home">
            <span className="brand-mark">
              <img src={qmoneyLogo} alt="QMoney logo" className="brand-logo" />
            </span>
            <span>QMoney</span>
          </a>

          <button
            type="button"
            className="icon-button menu-toggle-button"
            aria-label={menuLabel}
            aria-controls="site-navigation-panel"
            aria-expanded={isMobileMenuOpen}
            onClick={handleMenuToggle}
          >
            <MenuIcon open={isMobileMenuOpen} />
          </button>
        </div>

        <div
          id="site-navigation-panel"
          className="header-panel"
          role="region"
          aria-label="Site navigation panel"
          hidden={!isMobileMenuOpen}
        >
          <div className="header-controls">
            <nav className="site-nav" aria-label="Primary navigation">
              <a href="#intro" onClick={handleMobileNavClick}>Intro</a>
              <a href="#comparison" onClick={handleMobileNavClick}>Compare</a>
              <a href="#history" onClick={handleMobileNavClick}>History</a>
              <a href="#references" onClick={handleMobileNavClick}>References</a>
              <a href="#contact" onClick={handleMobileNavClick}>Join</a>
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
        </div>
      </header>

      <main id="top">
        <section className="hero">
          <p className="eyebrow">Quantum Computing + Bitcoin research</p>
          <h1>QMoney: A Peer-to-Peer Quantum Money System</h1>
          <p className="lede">
            Quantum money has been around since the late 1960s, and QMoney revisits that line of
            thought as a <strong>work-in-progress research repo for distributed private-key quantum cash</strong>.
            The goal is to pair a uniquely quantum anti-counterfeiting layer with a Bitcoin-inspired
            classical settlement layer.
          </p>
          <p className="lede lede-secondary">
            The current repo does <strong>not</strong> yet implement true public-key quantum money. Today it
            is best understood as <strong>quorum-verified private-key quantum cash</strong> with
            <strong> verify-and-remint</strong> semantics.
          </p>

          <div className="hero-actions">
            <a className="button button-primary" href="#intro">
              Read the intro
            </a>
            <a className="button button-secondary" href="#references">
              Browse references
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

        <section className="section" id="intro">
          <div className="section-copy">
            <p className="section-kicker">Intro</p>
            <p className="section-body">
              QMoney combines <strong>no-cloning</strong> at the quantum note layer with a
              <strong> Bitcoin-like classical settlement layer</strong> for ownership transfer,
              attestations, and spent-state tracking. It is intentionally honest about the split
              between the current private-key baseline and future public-key ambitions.
            </p>
          </div>

          <div className="architecture-grid">
            {introPoints.map((item, index) => (
              <article className={`panel${index === 0 ? ' panel-strong' : ''}`} key={item.title}>
                <h3>{item.title}</h3>
                <p>{item.body}</p>
              </article>
            ))}
          </div>

          <article className="panel warning-panel">
            <p className="panel-label">Current status</p>
            <h3>QMoney is still work-in-progress. There is no crypto token.</h3>
            <p>
              Near-term value in this repo is conceptual clarity, simulator design, attack modeling,
              note-family comparison, and architecture documentation—not near-term production deployment.
            </p>
          </article>
        </section>

        <section className="section" id="comparison">
          <div className="section-copy">
            <p className="section-kicker">Comparison</p>
            <p className="section-body">
              The repo has three useful mental models: the current private-key quorum baseline,
              the research-only public-key hidden-subspace track, and Bitcoin's production UTXO
              transaction model.
            </p>
          </div>

          <div className="comparison-table-wrap" role="region" aria-label="QMoney and Bitcoin comparison" tabIndex={0}>
            <table className="comparison-table">
              <thead>
                <tr>
                  <th scope="col">Dimension</th>
                  <th scope="col">pkey_quorum</th>
                  <th scope="col">pubkey_hidden_subspace</th>
                  <th scope="col">Standard BTC transaction</th>
                </tr>
              </thead>
              <tbody>
                {comparisonRows.map((row) => (
                  <tr key={row.dimension}>
                    <th scope="row">{row.dimension}</th>
                    <td>{row.pkey}</td>
                    <td>{row.pubkey}</td>
                    <td>{row.bitcoin}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="comparison-explainer">
            <article className="panel panel-strong">
              <p className="panel-label">Mental model</p>
              <h3>Private notes, public-verification research, and public ledger money are different layers.</h3>
              <p>
                pkey_quorum is private-banknote-style money built around bill serials, BB84 qubits,
                quorum-held secrets, and verify-and-remint transfers. pubkey_hidden_subspace explores
                public verification with hidden-subspace notes, but it is intentionally not a deployable
                unforgeability claim yet. Bitcoin is classical ledger money: UTXOs, signatures, public
                validation, and consensus inclusion.
              </p>
            </article>

            <article className="panel warning-panel comparison-caveat">
              <p className="panel-label">Key caveat</p>
              <h3>The hidden-subspace prototype is research-only.</h3>
              <p>
                Its current public key publishes enough structure to reconstruct an accepting note in
                software. That makes it useful for studying the public-verification workflow, not for
                claiming production-grade public-key quantum money.
              </p>
            </article>
          </div>
        </section>

        <section className="section" id="history">
          <div className="section-copy narrow">
            <p className="section-kicker">History</p>
            <h2>Historical background</h2>
          </div>

          <ol className="roadmap-list history-list">
            {historyPoints.map((item, index) => (
              <li className="roadmap-item" key={item}>
                <span className="roadmap-index">0{index + 1}</span>
                <p>{item}</p>
              </li>
            ))}
          </ol>
        </section>

        <section className="section" id="references">
          <div className="section-copy">
            <p className="section-kicker">References</p>
            <p className="section-body">
              These are the current architecture and research references highlighted in the README as
              the best entry points for understanding where QMoney stands today.
            </p>
          </div>

          <div className="reference-groups">
            {currentReferences.map((group) => (
              <article className="panel reference-panel" key={group.category}>
                <p className="panel-label">{group.category}</p>
                <div className="reference-list">
                  {group.items.map((item) => (
                    <a className="reference-link" href={item.href} key={item.href} target="_blank" rel="noreferrer">
                      <span className="reference-title">{item.title}</span>
                      <span className="reference-description">{item.description}</span>
                    </a>
                  ))}
                </div>
              </article>
            ))}
          </div>
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
