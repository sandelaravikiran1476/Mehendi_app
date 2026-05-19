"""
Beauty Tips Application with Category Filtering
Organized by skin type and beauty concerns
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class SkinType(Enum):
    """Skin type categories"""
    OILY = "Oily"
    DRY = "Dry"
    COMBINATION = "Combination"
    SENSITIVE = "Sensitive"
    NORMAL = "Normal"


class BeautyConcern(Enum):
    """Beauty concerns and issues"""
    ACNE = "Acne"
    AGING = "Aging"
    DARK_CIRCLES = "Dark Circles"
    HYPERPIGMENTATION = "Hyperpigmentation"
    DRYNESS = "Dryness"
    OILINESS = "Oiliness"
    SENSITIVITY = "Sensitivity"
    TEXTURE = "Texture"
    WRINKLES = "Wrinkles"
    PUFFINESS = "Puffiness"


@dataclass
class BeautyTip:
    """Represents a single beauty tip"""
    title: str
    description: str
    skin_types: List[SkinType]
    concerns: List[BeautyConcern]
    difficulty: str  # Easy, Moderate, Advanced
    
    def __str__(self) -> str:
        return (
            f"\n{'='*60}\n"
            f"💄 {self.title}\n"
            f"{'='*60}\n"
            f"Description: {self.description}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Best for Skin Types: {', '.join([st.value for st in self.skin_types])}\n"
            f"Addresses: {', '.join([c.value for c in self.concerns])}\n"
        )


class BeautyTipDatabase:
    """Database of beauty tips with filtering capabilities"""
    
    def __init__(self):
        self.tips = self._initialize_tips()
    
    def _initialize_tips(self) -> List[BeautyTip]:
        """Initialize the beauty tips database"""
        return [
            BeautyTip(
                title="Double Cleanse Method",
                description="Use an oil-based cleanser first to remove makeup and sunscreen, then follow with a water-based cleanser. This removes impurities without stripping natural oils.",
                skin_types=[SkinType.COMBINATION, SkinType.NORMAL, SkinType.OILY],
                concerns=[BeautyConcern.ACNE, BeautyConcern.TEXTURE],
                difficulty="Easy"
            ),
            BeautyTip(
                title="Retinol Layering Technique",
                description="Mix retinol with a hydrating serum to reduce irritation. Start with lowest concentration (0.03%) and gradually increase. Use 2-3 times per week initially.",
                skin_types=[SkinType.ALL if hasattr(SkinType, 'ALL') else SkinType.NORMAL],
                concerns=[BeautyConcern.AGING, BeautyConcern.WRINKLES],
                difficulty="Advanced"
            ),
            BeautyTip(
                title="Hydration Sandwich Method",
                description="Apply toner → essence → serum → moisturizer in quick succession while skin is still damp. This locks in hydration effectively.",
                skin_types=[SkinType.DRY, SkinType.SENSITIVE],
                concerns=[BeautyConcern.DRYNESS, BeautyConcern.SENSITIVITY],
                difficulty="Easy"
            ),
            BeautyTip(
                title="Spot Treatment with BHA",
                description="Apply salicylic acid (BHA) directly to acne-prone areas at night. BHA penetrates pores and reduces sebum buildup.",
                skin_types=[SkinType.OILY, SkinType.COMBINATION],
                concerns=[BeautyConcern.ACNE, BeautyConcern.OILINESS],
                difficulty="Moderate"
            ),
            BeautyTip(
                title="Vitamin C Serum Timing",
                description="Apply vitamin C serum to clean, dry skin before moisturizer. Use morning for antioxidant protection. Best efficacy at pH 3.5-4.0.",
                skin_types=[SkinType.NORMAL, SkinType.COMBINATION, SkinType.OILY],
                concerns=[BeautyConcern.AGING, BeautyConcern.HYPERPIGMENTATION],
                difficulty="Easy"
            ),
            BeautyTip(
                title="Cold Spoon for Dark Circles",
                description="Chill spoons in refrigerator overnight. Press on under-eye area for 2-3 minutes each morning to reduce puffiness and improve circulation.",
                skin_types=[SkinType.SENSITIVE, SkinType.NORMAL],
                concerns=[BeautyConcern.DARK_CIRCLES, BeautyConcern.PUFFINESS],
                difficulty="Easy"
            ),
            BeautyTip(
                title="Niacinamide for Pore Control",
                description="Use niacinamide serum (4-5%) to minimize pores and regulate sebum production. Works well with other actives.",
                skin_types=[SkinType.OILY, SkinType.COMBINATION],
                concerns=[BeautyConcern.OILINESS, BeautyConcern.TEXTURE],
                difficulty="Easy"
            ),
            BeautyTip(
                title="Gentle Exfoliation with AHA",
                description="Use glycolic acid (AHA) 2x weekly for dry skin, 1x weekly for oily skin. Apply to damp face for gentler exfoliation. Always use SPF 30+ after.",
                skin_types=[SkinType.DRY, SkinType.NORMAL],
                concerns=[BeautyConcern.TEXTURE, BeautyConcern.HYPERPIGMENTATION],
                difficulty="Moderate"
            ),
            BeautyTip(
                title="Hyaluronic Acid Layering",
                description="Apply hyaluronic acid serum on damp skin, then seal with moisturizer. HA can hold up to 1000x its weight in water.",
                skin_types=[SkinType.DRY, SkinType.SENSITIVE, SkinType.NORMAL],
                concerns=[BeautyConcern.DRYNESS],
                difficulty="Easy"
            ),
            BeautyTip(
                title="Sunscreen is Non-Negotiable",
                description="Apply broad-spectrum SPF 30+ every day, even indoors. Reapply every 2 hours if outdoors. This prevents aging and hyperpigmentation.",
                skin_types=[SkinType.NORMAL, SkinType.COMBINATION, SkinType.OILY, SkinType.DRY, SkinType.SENSITIVE],
                concerns=[BeautyConcern.AGING, BeautyConcern.HYPERPIGMENTATION],
                difficulty="Easy"
            ),
        ]
    
    def filter_by_skin_type(self, skin_type: SkinType) -> List[BeautyTip]:
        """Filter tips by skin type"""
        return [tip for tip in self.tips if skin_type in tip.skin_types]
    
    def filter_by_concern(self, concern: BeautyConcern) -> List[BeautyTip]:
        """Filter tips by beauty concern"""
        return [tip for tip in self.tips if concern in tip.concerns]
    
    def filter_by_difficulty(self, difficulty: str) -> List[BeautyTip]:
        """Filter tips by difficulty level"""
        return [tip for tip in self.tips if tip.difficulty == difficulty]
    
    def filter_multiple(self, 
                       skin_type: Optional[SkinType] = None,
                       concern: Optional[BeautyConcern] = None,
                       difficulty: Optional[str] = None) -> List[BeautyTip]:
        """Filter by multiple criteria"""
        results = self.tips
        
        if skin_type:
            results = [tip for tip in results if skin_type in tip.skin_types]
        
        if concern:
            results = [tip for tip in results if concern in tip.concerns]
        
        if difficulty:
            results = [tip for tip in results if tip.difficulty == difficulty]
        
        return results
    
    def display_all(self) -> None:
        """Display all tips"""
        print("\n" + "="*60)
        print("🌟 COMPLETE BEAUTY TIPS DATABASE 🌟")
        print("="*60)
        for tip in self.tips:
            print(tip)
    
    def display_filtered(self, tips: List[BeautyTip], filter_name: str) -> None:
        """Display filtered results"""
        if not tips:
            print(f"\n❌ No tips found for {filter_name}")
            return
        
        print(f"\n{'='*60}")
        print(f"✨ Results for: {filter_name}")
        print(f"{'='*60}")
        print(f"Found {len(tips)} tip(s)\n")
        for tip in tips:
            print(tip)


def interactive_menu():
    """Interactive menu for filtering beauty tips"""
    db = BeautyTipDatabase()
    
    while True:
        print("\n" + "="*60)
        print("💅 BEAUTY TIPS FINDER 💅")
        print("="*60)
        print("1. Filter by Skin Type")
        print("2. Filter by Beauty Concern")
        print("3. Filter by Difficulty Level")
        print("4. Combined Filter (Multiple Criteria)")
        print("5. View All Tips")
        print("6. Exit")
        print("="*60)
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            print("\nAvailable Skin Types:")
            for i, skin_type in enumerate(SkinType, 1):
                print(f"  {i}. {skin_type.value}")
            
            try:
                skin_choice = int(input("Select skin type number: "))
                selected_skin = list(SkinType)[skin_choice - 1]
                results = db.filter_by_skin_type(selected_skin)
                db.display_filtered(results, f"Skin Type: {selected_skin.value}")
            except (ValueError, IndexError):
                print("Invalid selection.")
        
        elif choice == "2":
            print("\nAvailable Beauty Concerns:")
            for i, concern in enumerate(BeautyConcern, 1):
                print(f"  {i}. {concern.value}")
            
            try:
                concern_choice = int(input("Select concern number: "))
                selected_concern = list(BeautyConcern)[concern_choice - 1]
                results = db.filter_by_concern(selected_concern)
                db.display_filtered(results, f"Concern: {selected_concern.value}")
            except (ValueError, IndexError):
                print("Invalid selection.")
        
        elif choice == "3":
            print("\nAvailable Difficulty Levels:")
            print("  1. Easy")
            print("  2. Moderate")
            print("  3. Advanced")
            
            difficulty_map = {1: "Easy", 2: "Moderate", 3: "Advanced"}
            try:
                diff_choice = int(input("Select difficulty number: "))
                selected_difficulty = difficulty_map[diff_choice]
                results = db.filter_by_difficulty(selected_difficulty)
                db.display_filtered(results, f"Difficulty: {selected_difficulty}")
            except (ValueError, KeyError):
                print("Invalid selection.")
        
        elif choice == "4":
            print("\nCombined Filter:")
            
            # Skin type selection
            print("\nSkin Types (press Enter to skip):")
            for i, skin_type in enumerate(SkinType, 1):
                print(f"  {i}. {skin_type.value}")
            skin_input = input("Select skin type number (or press Enter): ").strip()
            skin_type = None
            if skin_input:
                try:
                    skin_type = list(SkinType)[int(skin_input) - 1]
                except (ValueError, IndexError):
                    print("Invalid skin type selection.")
            
            # Concern selection
            print("\nConcerns (press Enter to skip):")
            for i, concern in enumerate(BeautyConcern, 1):
                print(f"  {i}. {concern.value}")
            concern_input = input("Select concern number (or press Enter): ").strip()
            concern = None
            if concern_input:
                try:
                    concern = list(BeautyConcern)[int(concern_input) - 1]
                except (ValueError, IndexError):
                    print("Invalid concern selection.")
            
            # Difficulty selection
            print("\nDifficulty (press Enter to skip):")
            print("  1. Easy")
            print("  2. Moderate")
            print("  3. Advanced")
            difficulty_input = input("Select difficulty number (or press Enter): ").strip()
            difficulty = None
            difficulty_map = {1: "Easy", 2: "ss", 3: "Advanced"}
            if difficulty_input:
                try:
                    difficulty = difficulty_map[int(difficulty_input)]
                except (ValueError, KeyError):
                    print("Invalid difficulty selection.")
            
            results = db.filter_multiple(skin_type, concern, difficulty)
            filter_desc = " + ".join(filter(None, [
                f"Skin: {skin_type.value}" if skin_type else None,
                f"Concern: {concern.value}" if concern else None,
                f"Difficulty: {difficulty}" if difficulty else None
            ]))
            db.display_filtered(results, filter_desc)
        
        elif choice == "5":
            db.display_all()
        
        elif choice == "6":
            print("\n👋 Goodbye! Keep your skin glowing!\n")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    # Run interactive menu
    interactive_menu()
