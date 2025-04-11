"""Add hashed_password to User

Revision ID: 3f44515e8cd8
Revises: 7069f9d1fe09
Create Date: 2025-04-10 22:10:33.654440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f44515e8cd8'
down_revision: Union[str, None] = '7069f9d1fe09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=True))
    op.execute("UPDATE users SET full_name = 'Temporary Name' WHERE full_name IS NULL")

    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))
    # Add temporary default password hash to existing rows (not secure, just to pass NOT NULL!)
    op.execute("UPDATE users SET hashed_password = 'temp-hash-placeholder' WHERE hashed_password IS NULL")
    # Then alter column to set NOT NULL
    op.alter_column('users', 'hashed_password', nullable=False)
    
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.execute("UPDATE users SET is_active = TRUE WHERE is_active IS NULL")
    op.alter_column('users', 'is_active', nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'hashed_password')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###
