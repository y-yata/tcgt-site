---
title: Privacy Policy | TCG-T
---

# Privacy Policy

Last updated: 2026-09-25

This policy explains how the mobile app "TCG-T" (the "App") handles your information.

---

## 1. Summary

- **No account registration.** While you use the App without signing in, we do not collect your name, email address or phone number.
- **Only if you sign in with Apple or Google do we receive that account's email address (or the relay address Apple issues if you choose "Hide My Email") and an identifier.** We use them only to keep your point balance and decoration entitlements across devices.
- **Cards, decks, game settings and images you create stay on your device.**
- We send to servers only: **images you submit to the AI autofill**, **the cards of a deck you use in an online match (only during the match)**, **point balance and related records**, **account information if you sign in**, and **optional usage analytics**.
- The App shows ads (Google AdMob). You can refuse the use of advertising identifiers through the OS setting and the consent screen.

## 2. What we collect and why

### 2-1. Stored only on your device (never sent)

| Data | Examples |
|---|---|
| Game settings | Attributes, deck structure, board design, rules |
| Card data | Card name, code, attributes, **card images** |
| Decks | Composition, cover card, decorations such as sleeves |
| Solo run state | Board layout, turn count, saved runs |
| App settings | Language, theme, number of columns |

These are kept in the App's own storage and file area on your device.
**Deleting the App removes them from the device.**

### 2-2. Sent to servers

| Data | Recipient | Purpose | Notes |
|---|---|---|---|
| Anonymous account identifier (a random ID) | Our server (Supabase) | Keeping point balance and decoration entitlements per user | Not linked to your name |
| **If you sign in:** email address and sign-in identifier (Apple / Google) | Our server (Supabase) | Keeping the same point balance and decoration entitlements after changing devices or reinstalling | Signing in is optional. We do not store your name |
| Point transaction history | Our server | Calculating balance, preventing duplicate or fraudulent grants | Amount, reason, timestamp |
| AI usage records | Our server | Enforcing rate limits, tracking operating costs | Timestamp and processing volume (no image or result content) |
| **Card images** | Anthropic, via our server | Autofilling card name, code and attributes (only when you start it) | Our server does not store them |
| Decoration entitlements and expiry | Our server | Recording what you exchanged points for | The images themselves are not sent |
| Cards of a deck used in an **online match** (name, attributes, card images) | Our server (Supabase) | Showing your cards on your opponent's screen | Visible only to your opponent. Deleted automatically when the table is closed or after it expires (at most 3 hours) |
| Purchase records (product and time) | RevenueCat | Verifying in-app purchases and granting points / Premium | We do not receive payment details such as card numbers |
| Advertising identifier, device information, approximate location (from IP) | Google | Serving and measuring ads | See section 3 |
| Usage analytics (screens viewed, feature counts) | PostHog | Understanding and fixing problems | Can be turned off in settings |

**The AI feature sends an image only when you tap "Autofill with AI".** The App never sends images on its own.

## 3. Advertising

The App shows ads through Google AdMob (not shown while a paid plan is active).

- To serve and measure ads, your **advertising identifier (IDFA on iOS / Advertising ID on Android), device information and approximate location based on IP address** may be sent to Google.
- **On iOS, we ask for tracking permission on first launch.** If you refuse, the identifier is not used (ads still appear, but they are not selected based on you).
- **In the European Economic Area and the UK we ask for your consent** before using data for advertising. If you do not consent, we do not use it. You can change your choice at any time from **Settings → Ads → Ad privacy settings**.
- Watching a rewarded video to the end grants points. That is confirmed by a notification from Google and applied on our server.

Please also refer to Google's own policies for how Google handles this data.

## 4. Service providers

We use the services below and do not share your data beyond these purposes.

| Provider | Use |
|---|---|
| Supabase | Accounts (anonymous / signed in), point ledger, online matches, server functions |
| Anthropic | Extracting attributes from card images (AI) |
| Google (AdMob) | Ad serving and measurement, consent management |
| PostHog | Usage analytics |
| Apple / Google (app stores) | Payment processing |
| Apple / Google (sign-in) | Identity verification if you choose to sign in |
| RevenueCat | Verifying in-app purchases |

These providers may operate servers outside your country.

## 5. Retention

- Data on your device is kept until you delete it or delete the App.
- The point ledger and decoration entitlements on our server are kept **until the account is deleted**, because they determine your balance and rights.
- AI usage records are only needed for the rate-limit window.
- **Card images sent to the AI autofill are used for processing only and are not stored on our server.**
- Cards uploaded for an online match are deleted automatically when the table is closed or after it expires (at most 3 hours).
- Account information from signing in is kept until the account is deleted.

## 6. Your choices

| Goal | How |
|---|---|
| Stop sending usage analytics | Settings → Privacy → turn off "Share usage data" |
| Refuse ad tracking (iOS) | Decline the first-launch prompt, or OS Settings → Privacy & Security → Tracking |
| Change ad consent (EEA/UK) | Settings → Ads → Ad privacy settings |
| Delete data on your device | Delete items in the App, or delete the App |
| Delete your account and server-side data (if signed in) | Settings → Account → "Delete TCG-T account" |
| Request deletion of other server-side data | Contact us using the address below |

**Note:** While you use the App without signing in, the account is created anonymously. **If you delete the App, the point balance and decoration entitlements of that account cannot be restored.** Signing in with Apple or Google lets you keep them.

## 7. Children

The App is not directed to children. If you are a parent or guardian with concerns about your child's use, please contact us.

## 8. Security

- Traffic is encrypted (HTTPS).
- Server-side data is restricted so that **only your own account can read it** (row-level access control).
- Points and entitlements can only be granted by the server, never by the app itself.

## 9. Changes to this policy

If we change this policy, we will post the updated text and date on this page, and notify significant changes in the App.

## 10. Contact

tcg.training.app@gmail.com

Requests to be notified of the purpose of use, or to disclose, correct or stop using your
retained personal data, are also handled at this address.

## 11. Business information

| Item | Detail |
|---|---|
| Business name | AIyabane |
| Representative | Yoshiki Yatagai |
| Address | 2F-C Shibuya Dogenzaka Tokyu Building, 1-10-8 Dogenzaka, Shibuya-ku, Tokyo 150-0043, Japan |
| Contact for personal data matters | tcg.training.app@gmail.com |

Published in accordance with Article 32 of Japan's Act on the Protection of Personal Information.
