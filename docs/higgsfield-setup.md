# Higgsfield Supercomputer — local setup

Higgsfield "Supercomputer" is a cloud-native service (image, video, and
Marketing Studio generation). There is nothing to self-host: all compute runs
on Higgsfield's cloud. What you install locally is the **Higgsfield CLI**,
which lets you (and your coding agents) drive that cloud from the terminal.

## 1. Install the CLI

Requires Node.js 18+ and npm.

```bash
npm install -g @higgsfield/cli
```

The postinstall step downloads a prebuilt `hf` binary for your platform
(macOS, Linux, Windows — x64/arm64). Verify with:

```bash
higgsfield --version
```

Aliases: `higgsfield`, `higgs`, `hf`.

## 2. Authenticate

Authentication uses browser-based OAuth (PKCE), so run this on a machine with
a web browser:

```bash
higgsfield auth login
```

Complete the sign-in in the browser that opens. Credentials are stored
locally; `higgsfield auth token` prints the current access token, and
`higgsfield auth logout` removes it.

On a headless machine (server, container), authenticate on your desktop first
and copy the credentials file over, pointing `HIGGSFIELD_CREDENTIALS_PATH` at
it if you place it somewhere non-default.

## 3. Try it

```bash
higgsfield model list                 # available image/video models
higgsfield workflow list              # available workflows
higgsfield generate create text2image_soul_v2 --prompt "a cat in a spaceship"
higgsfield account                    # credits and transactions
```

Add `--json` to any command for machine-readable output (useful for agents).

## 4. Optional: agent skills

Higgsfield publishes companion skills for coding agents:

```bash
npx skills add higgsfield-ai/skills
```

These teach an agent how to use the CLI for generation workflows
(product photoshoots, marketing assets, video, etc.).

## Notes

- Generation consumes Higgsfield credits tied to the logged-in account;
  check balances with `higgsfield account`.
- Useful environment variables: `HIGGSFIELD_CREDENTIALS_PATH`,
  `HIGGSFIELD_CONFIG_PATH`, `HIGGSFIELD_DISABLE_TELEMETRY`,
  `HIGGSFIELD_WORKSPACE_ID`.
