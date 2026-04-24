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
          <a href="#roadmap">Roadmap</a>
          <a href="#contact">Join</a>
        </nav>
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
