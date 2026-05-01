# QMoney website

This folder contains the Vite + React + TypeScript landing page for QMoney.

The site is a public explanation layer for the repository. It should keep the same boundaries as the core docs:

- QMoney is currently a **work-in-progress research project**, not a production token, wallet, or currency.
- The implemented baseline is **distributed private-key quantum cash** with verify-and-remint semantics.
- The public-key hidden-subspace path is a **research-only prototype** and not a deployable unforgeability claim.
- Bitcoin is used as a settlement/finality reference point, not as a claim that QMoney is already “quantum Bitcoin.”

## Local development

Install dependencies from this folder:

```bash
npm ci
```

Run the development server:

```bash
npm run dev
```

Build the static site:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview -- --host 127.0.0.1 --port 4173
```

## Verification

Before committing website changes, run:

```bash
npm run build
npm run lint
npm run test
```

Current test coverage lives in `src/App.test.tsx` and checks the main messaging, reference links, theme behavior, and menu interactions.

## Content rules

When editing the website copy:

1. Preserve the distinction between the private-key baseline and public-key research track.
2. Avoid implying that the current repo implements production quantum hardware.
3. Avoid implying that the hidden-subspace prototype is secure public-key quantum money.
4. Keep “verify-and-remint” visible as the current transfer model.
5. Link deeper claims back to the repository docs, especially:
   - `docs/architecture/public-vs-private-key-qmoney.md`
   - `docs/architecture/private-key-quorum-threat-model.md`
   - `docs/research/latest-quantum-money-literature-and-qmoney.md`

## Deployment note

This is a static Vite site. `npm run build` writes output to `dist/`. The generated `dist/` directory is intentionally ignored by git.
