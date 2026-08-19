---
title: Privacy Policy | TCG-T
---

# Privacy Policy

Last updated: 2026-08-19

This policy explains how the mobile app "TCG-T" (the "App") handles your information.

## 1. Summary

- **No account registration.** We do not collect your name, email address or phone number.
- **Cards, decks, game settings and images you create stay on your device.**
- We send to servers only: **images you submit to the AI autofill**, **point balance and related records**, and **optional usage analytics**.
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
| Point transaction history | Our server | Calculating balance, preventing duplicate or fraudulent grants | Amount, reason, timestamp |
| AI usage records | Our server | Enforcing rate limits | Timestamp only |
| **Card images** | Anthropic, via our server | Autofilling card name and attributes (only when you start it) | Our server does not store them |
| Decoration entitlements and expiry | Our server | Recording what you exchanged points for | The images themselves are not sent |
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
| Supabase | Anonymous accounts, point ledger, server functions |
| Anthropic | Extracting attributes from card images (AI) |
| Google (AdMob) | Ad serving and measurement, consent management |
| PostHog | Usage analytics |
| Apple / Google (app stores) | Payment processing |

These providers may operate servers outside your country.

## 5. Retention

- Data on your device is kept until you delete it or delete the App.
- The point ledger and decoration entitlements on our server are kept **until the account is deleted**, because they determine your balance and rights.
- AI usage records are only needed for the rate-limit window.
- **Card images are sent for processing only and are not stored on our server.**

## 6. Your choices

| Goal | How |
|---|---|
| Stop sending usage analytics | Settings → Privacy → turn off "Share usage data" |
| Refuse ad tracking (iOS) | Decline the first-launch prompt, or OS Settings → Privacy & Security → Tracking |
| Change ad consent (EEA/UK) | Settings → Ads → Ad privacy settings |
| Delete data on your device | Delete items in the App, or delete the App |
| Request deletion of server-side data | Contact us using the address below |

**Note:** Accounts are created anonymously. **If you delete the App, the point balance and decoration entitlements of that account cannot be restored.**

## 7. Children

The App is not directed to children. If you are a parent or guardian with concerns about your child's use, please contact us.

## 8. Security

- Traffic is encrypted (HTTPS).
- Server-side data is restricted so that **only your own account can read it** (row-level access control).
- Points and entitlements can only be granted by the server, never by the app itself.

## 9. Changes to this policy

If we change this policy, we will post the updated text and date on this page, and notify significant changes in the App.

## 10. Provider and contact

Provider: Yoshiki Yatagai (individual developer)  
Contact: tcg.training.app@gmail.com
