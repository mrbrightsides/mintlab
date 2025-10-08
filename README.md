# 💻 MintLab - Browser-Based Smart Contract IDE

**MintLab** is a modern, browser-based IDE for creating, customizing, and deploying ERC20 and ERC721 smart contracts directly to multiple blockchain networks. Built with Next.js and powered by ThirdWeb, MintLab makes Web3 development accessible to everyone.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Next.js](https://img.shields.io/badge/Next.js-14.0-black)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)](https://www.typescriptlang.org/)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mintlab.streamlit.app/)
![RANTAI Lab – MintLab](https://img.shields.io/badge/RANTAI%20Lab-MintLab-orangered)
![status: stable](https://img.shields.io/badge/status-stable-brightgreen)

---

## ✨ Features

### 🎨 **Modern IDE Experience**
- **Monaco-style Code Editor** with syntax highlighting for Solidity
- **Real-time Error Detection** with inline validation
- **Code Auto-Complete** for faster development
- **Theme Switcher** (Light/Dark modes)
- **Full-Screen Mode** for distraction-free coding

### 🔗 **Multi-Network Support**
Deploy your contracts to multiple networks:
- Ethereum Sepolia Testnet
- Polygon Mumbai/Amoy
- Binance Smart Chain Testnet
- Arbitrum Sepolia
- Base Sepolia

### 🤖 **AI-Powered Assistant**
- Integrated **Perplexity AI** for code explanation
- Smart error correction suggestions
- Contract optimization recommendations
- Real-time coding help

### 💎 **Smart Contract Templates**
- **ERC20 Tokens**: Standard, Mintable, Burnable, Capped
- **ERC721 NFTs**: Basic, Enumerable, URI Storage, Auto-Increment
- **Advanced Features**: Pausable, Ownable, AccessControl
- **Custom Templates**: Build your own from scratch

### ⚡ **Advanced Features**
- **Gas Estimation** before deployment
- **Contract Verification** on block explorers
- **MetaMask Integration** for seamless wallet connection
- **Deployment History** tracking
- **IPFS Integration** via Pinata for metadata storage
- **SCT Marketplace** integration for smart contract templates

### 📱 **Responsive Design**
- Fully optimized for desktop and mobile devices
- Dark theme with purple-blue gradients
- Neon green highlights for futuristic aesthetic
- Clean, minimalistic UI/UX

---

## 📊 Demo UI

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d09183d4-7bc5-4210-a993-8ed9bcb4d9eb" /><br>

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/dca265f3-0921-45d3-9273-f5fc289a273c" />

---

## 🛠️ Tech Stack

- **Framework**: [Next.js 14](https://nextjs.org/) with App Router
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Web3**: [ThirdWeb SDK](https://thirdweb.com/)
- **Editor**: Monaco Editor (VS Code engine)
- **AI**: Perplexity API
- **Storage**: IPFS via [Pinata](https://pinata.cloud/)
- **UI Components**: Radix UI, Lucide Icons

---

## 🚀 Getting Started

### Prerequisites

- Node.js 18.x or higher
- npm or yarn
- MetaMask wallet extension

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mintlab.git
   cd mintlab
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   Create a `.env.local` file in the root directory:
   ```env
   NEXT_PUBLIC_THIRDWEB_CLIENT_ID=your_thirdweb_client_id
   ```

4. **Run the development server**
   ```bash
   npm run dev
   ```

5. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

---

## 📖 Usage

### Creating an ERC20 Token

1. Navigate to **ERC20 Editor** from the homepage
2. Choose a template (Standard, Mintable, Burnable, Capped)
3. Customize token parameters:
   - Token Name
   - Symbol
   - Initial Supply
   - Decimals
4. Edit the Solidity code if needed
5. Select target network
6. Click **Deploy Contract**
7. Confirm transaction in MetaMask

### Creating an ERC721 NFT Collection

1. Navigate to **ERC721 Editor** from the homepage
2. Choose a template (Basic, Enumerable, URI Storage)
3. Customize NFT parameters:
   - Collection Name
   - Symbol
   - Base URI (optional)
4. Edit the Solidity code in the Monaco editor
5. Select deployment network
6. Click **Deploy Contract**
7. Approve the transaction in MetaMask

### Using AI Assistant

1. Click the **AI Assistant** button in the editor
2. Type your question about Solidity or your contract
3. Get instant explanations, suggestions, and error fixes
4. Apply suggested fixes directly to your code

---

## 🎯 Roadmap

- [x] ERC20 & ERC721 token deployment
- [x] Multi-network support
- [x] AI-powered coding assistant
- [x] Gas estimation
- [x] Contract verification
- [x] Template marketplace integration
- [ ] ERC1155 multi-token standard support
- [ ] Contract testing framework
- [ ] Code versioning and Git integration
- [ ] Collaborative editing (real-time)
- [ ] Custom ABI import/export
- [ ] Mainnet deployment support

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **ThirdWeb** for the powerful Web3 SDK
- **Monaco Editor** for the VS Code-like editing experience
- **Perplexity AI** for intelligent code assistance
- **Pinata** for decentralized storage solutions
- **SCT Marketplace** for smart contract templates

---

## 📞 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/mrbrightsides/mintlab/issues)
- **Email**: support@elpeef.com
- **Web**: [ELPEEF](https://elpeef.com)

---

## 🌟 Show Your Support

If you find MintLab useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🔄 Sharing with the Web3 community

---

<div align="center">
  <p>Built with ❤️ by the ELPEEF Team</p>
  <p>© 2025 MintLab. All rights reserved.</p>
</div>

