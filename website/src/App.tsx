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

const distinctions = [
  {
    title: 'What QMoney is today',
    body: 'A quorum-verified, private-key quantum cash system with a classical public-key settlement layer.',
  },
  {
    title: 'What it is not yet',
    body: 'It is not a finished public-key quantum money system where anyone can verify from public information without learning how to mint valid notes.',
  },
  {
    title: 'Why that matters',
    body: 'Private-key and public-key quantum money require different note families, different verifier models, and different security stories.',
  },
]

const roadmap = [
  'Preserve the current private-key baseline as an honest reference architecture for transfer, remint, and counterfeit modeling.',
  'Explore separate public-key note families—starting with hidden-subspace prototypes—without pretending the BB84 baseline is already public-key.',
  'Keep new claims grounded with tests, lifecycle invariants, and symbolic checks so conceptual progress stays legible.',
]

const docs = [
  {
    title: 'Architecture note',
    href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/public-vs-private-key-qmoney.md',
    body: 'Why QMoney is currently private-key quantum cash rather than public-key quantum money.',
  },
  {
    title: 'Quorum baseline',
    href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/software-mps-quorum-design.md',
    body: 'The software-only BB84 baseline, including quorum verification and verify-and-remint semantics.',
  },
  {
    title: 'Hidden-subspace notes',
    href: 'https://github.com/runeape-sats/qmoney/blob/main/docs/research/hidden-subspace-notes.md',
    body: 'The current research-only public-key verifier sketch and its documented limitations.',
  },
]

function App() {
  return (
    <div className="page">
      <header className="site-header">
        <a className="brand" href="#top" aria-label="QMoney home">
          <span className="brand-mark">Q</span>
          <span>QMoney</span>
        </a>

        <nav className="site-nav" aria-label="Primary navigation">
          <a href="#premise">Premise</a>
          <a href="#distinction">Distinction</a>
          <a href="#docs">Docs</a>
          <a href="#roadmap">Roadmap</a>
        </nav>
      </header>

      <main id="top">
        <section className="hero">
          <p className="eyebrow">Quantum cash research</p>
          <h1>QMoney asks a simple question: can unclonable quantum notes and distributed settlement live in the same money architecture?</h1>
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
            <a className="button button-secondary" href="#docs">
              Open the docs
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

        <section className="section" id="distinction">
          <div className="section-copy narrow">
            <p className="section-kicker">Distinction</p>
            <h2>The most important thing QMoney does is keep its claims honest.</h2>
          </div>

          <div className="principles-list">
            {distinctions.map((item) => (
              <article className="principle-row" key={item.title}>
                <h3>{item.title}</h3>
                <p>{item.body}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="section" id="docs">
          <div className="section-copy narrow">
            <p className="section-kicker">Docs</p>
            <h2>If you want the full argument, start with the architecture docs and follow outward.</h2>
          </div>

          <div className="architecture-grid docs-grid">
            {docs.map((doc) => (
              <article className="panel doc-panel" key={doc.title}>
                <h3>{doc.title}</h3>
                <p>{doc.body}</p>
                <a className="doc-link" href={doc.href} target="_blank" rel="noreferrer">
                  Open on GitHub
                </a>
              </article>
            ))}
          </div>
        </section>

        <section className="section" id="roadmap">
          <div className="section-copy narrow">
            <p className="section-kicker">Roadmap</p>
            <h2>Move carefully: keep the baseline honest, then earn stronger claims later.</h2>
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
          <p className="section-kicker">Bottom line</p>
          <h2>QMoney is already a coherent quantum cash architecture, even before the public-key story is finished.</h2>
          <p>
            The point is not to overclaim. The point is to preserve the current private-key baseline,
            explain it clearly, and build any future public-key work as a genuinely separate note
            family and security story.
          </p>
        </section>
      </main>
    </div>
  )
}

export default App
